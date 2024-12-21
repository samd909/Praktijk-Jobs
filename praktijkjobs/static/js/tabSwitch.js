function showTab(tabId, activeButtonId) {
    // Hide all tab contents
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));

    // Remove active styles from buttons
    document.querySelectorAll('.border-b-2').forEach(button => {
        button.classList.remove('border-blue-500', 'text-blue-500');
        button.classList.add('text-gray-500');
    });

    // Show the selected tab
    document.getElementById(tabId).classList.remove('hidden');

    // Add active styles to the selected button
    document.getElementById(activeButtonId).classList.add('border-blue-500', 'text-blue-500');
}