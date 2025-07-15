document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const payload = {
        location: document.getElementById('location').value,
        total_sqft: parseFloat(document.getElementById('total_sqft').value),
        bath: parseInt(document.getElementById('bath').value),
        bedroom: parseInt(document.getElementById('bedroom').value)
    };

    try {
        const response = await fetch('http://localhost:8000/predict_house_price', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error('Prediction failed');
        
        const result = await response.json();
        document.getElementById('price').textContent = result.price.toLocaleString('en-IN');
        document.getElementById('result').classList.remove('hidden');
    } catch (error) {
            alert(`Error: ${error.message}`);
    }
});

// Fetch locations from backend API
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('http://localhost:8000/get_locations');
        const locations = await response.json();
        const locationSelect = document.getElementById('location');
        
        locations.forEach(location => {
            const option = document.createElement('option');
            option.value = location;
            option.textContent = location;
            locationSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error loading locations:', error);
    }
});