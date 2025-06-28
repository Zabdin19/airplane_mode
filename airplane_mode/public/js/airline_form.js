frappe.web_form.on('airline', {
    after_render: function () {
        const website = frappe.web_form.get_value('website');

        if (website && website.trim() !== "" && website !== "undefined") {
            const linkElement = document.createElement('a');
            linkElement.href = website.startsWith('http') ? website : 'https://' + website;
            linkElement.target = '_blank';
            linkElement.textContent = 'Visit Airline Website';
            linkElement.style.display = 'inline-block';
            linkElement.style.marginTop = '10px';
            linkElement.style.color = '#1d72b8';
            linkElement.style.fontWeight = 'bold';

            const wrapper = document.querySelector('.web-form-actions');
            if (wrapper) {
                wrapper.appendChild(linkElement);
            }
        }
    }
});
