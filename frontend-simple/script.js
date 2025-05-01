document.addEventListener('DOMContentLoaded', () => {
    const medicalText = document.getElementById('medicalText');
    const detectBtn = document.getElementById('detectBtn');
    const results = document.getElementById('results');
    const diseaseList = document.getElementById('diseaseList');
    const loading = document.querySelector('.loading');
    const pdfFile = document.getElementById('pdfFile');
    const fileName = document.getElementById('fileName');

    // Handle PDF file selection
    pdfFile.addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            fileName.textContent = file.name;
            // Clear text area when file is selected
            medicalText.value = '';
        } else {
            fileName.textContent = 'No file chosen';
        }
    });

    // Handle text input
    medicalText.addEventListener('input', () => {
        // Clear file selection when text is entered
        if (medicalText.value.trim()) {
            pdfFile.value = '';
            fileName.textContent = 'No file chosen';
        }
    });

    detectBtn.addEventListener('click', async () => {
        const text = medicalText.value.trim();
        const file = pdfFile.files[0];
        
        if (!text && !file) {
            alert('Please enter text or upload a PDF file');
            return;
        }

        // Show loading state
        loading.style.display = 'block';
        diseaseList.innerHTML = '';

        try {
            let response;
            if (file) {
                // Handle PDF file
                const formData = new FormData();
                formData.append('file', file);
                
                response = await fetch('http://localhost:5000/predict_pdf', {
                    method: 'POST',
                    body: formData
                });
            } else {
                // Handle text input
                response = await fetch('http://localhost:5000/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: text })
                });
            }

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            
            // Clear previous results
            diseaseList.innerHTML = '';

            // Display results
            if (data.diseases && data.diseases.length > 0) {
                data.diseases.forEach(disease => {
                    const diseaseElement = document.createElement('div');
                    diseaseElement.className = 'disease-item';
                    diseaseElement.textContent = disease;
                    diseaseList.appendChild(diseaseElement);
                });
            } else {
                diseaseList.innerHTML = '<div class="disease-item">No diseases detected in the text.</div>';
            }
        } catch (error) {
            console.error('Error:', error);
            diseaseList.innerHTML = '<div class="disease-item" style="color: red;">Error: Could not connect to the server. Please make sure the backend is running.</div>';
        } finally {
            loading.style.display = 'none';
        }
    });

    // Add example text button
    const exampleBtn = document.getElementById('exampleBtn');
    exampleBtn.addEventListener('click', () => {
        medicalText.value = 'Patient presents with symptoms of diabetes mellitus including increased thirst, frequent urination, and fatigue. History of hypertension and coronary artery disease.';
        // Clear file selection when example is loaded
        pdfFile.value = '';
        fileName.textContent = 'No file chosen';
    });
}); 