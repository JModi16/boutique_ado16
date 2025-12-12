let countrySelected = document.getElementById('id_default_country');
let countryDisplay = document.querySelector('[data-last-value]');

// Set the country select widget's default value
if (countrySelected) {
    countrySelected.addEventListener('change', function() {
        let countryCodeElement = document.querySelector('[data-last-value]');
        if (countryCodeElement) {
            countryCodeElement.textContent = this.value;
        }
    });
}

// Handle initial display value
document.addEventListener('DOMContentLoaded', function() {
    if (countrySelected && countrySelected.value) {
        if (countryDisplay) {
            countryDisplay.textContent = countrySelected.value;
        }
    }
});