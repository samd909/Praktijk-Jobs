   // Get modal elements
   const openModalButton = document.getElementById('openModalButton');
   const closeModalButton = document.getElementById('closeModalButton');
   const modal = document.getElementById('modal');
   
   // Open modal when the "Nieuw Verzoek" button is clicked
   openModalButton.addEventListener('click', function() {
       modal.classList.remove('hidden'); // Show modal
   });
   
   // Close modal when the "Sluiten" button is clicked
   closeModalButton.addEventListener('click', function() {
       modal.classList.add('hidden'); // Hide modal
   });

   // Optional: Close modal when clicking outside the modal
   window.addEventListener('click', function(event) {
       if (event.target === modal) {
           modal.classList.add('hidden'); // Hide modal when clicked outside
       }
   });