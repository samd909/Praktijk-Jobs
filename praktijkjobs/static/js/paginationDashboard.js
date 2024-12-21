 // Initialize page index and number of rows per page
 const rowsPerPage = 5;

 // Function to paginate posts
 function paginatePosts(tableId, prevButtonId, nextButtonId) {
     const table = document.getElementById(tableId);
     const rows = table.querySelectorAll('tr');
     const totalPages = Math.ceil(rows.length / rowsPerPage);
     let currentPage = 1;

     // Function to show the posts for the current page
     function showPage(pageNumber) {
         const startIndex = (pageNumber - 1) * rowsPerPage;
         const endIndex = pageNumber * rowsPerPage;

         rows.forEach((row, index) => {
             if (index >= startIndex && index < endIndex) {
                 row.classList.remove('hidden');
             } else {
                 row.classList.add('hidden');
             }
         });

         // Disable/enable the pagination buttons
         document.getElementById(prevButtonId).disabled = pageNumber === 1;
         document.getElementById(nextButtonId).disabled = pageNumber === totalPages;
     }

     // Event listeners for Previous and Next buttons
     document.getElementById(prevButtonId).addEventListener('click', () => {
         if (currentPage > 1) {
             currentPage--;
             showPage(currentPage);
         }
     });

     document.getElementById(nextButtonId).addEventListener('click', () => {
         if (currentPage < totalPages) {
             currentPage++;
             showPage(currentPage);
         }
     });

     // Initialize the first page
     showPage(currentPage);
 }

 // Initialize pagination for Open and Closed posts
 window.addEventListener('DOMContentLoaded', () => {
     paginatePosts('openPostsTable', 'prevPage', 'nextPage');
     paginatePosts('closedPostsTable', 'prevClosedPage', 'nextClosedPage');
 });