document.addEventListener('DOMContentLoaded', function() {
    // Initialize Materialize components
    M.AutoInit();

    // Form validation
    const addPlantForm = document.getElementById('add-plant-form');
    if (addPlantForm) {
        addPlantForm.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const watering = document.getElementById('watering').value;
            const environment = document.getElementById('environment').value;
            const careLevel = document.getElementById('care_level').value;

            if (!name || !watering || !environment || !careLevel) {
                event.preventDefault();
                M.toast({html: 'Please fill in all required fields'});
            }
        });
    }
});