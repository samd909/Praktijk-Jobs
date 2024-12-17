       // JavaScript for tab switching
       const openTab = document.getElementById('openTab');
       const closedTab = document.getElementById('closedTab');
       const openPosts = document.getElementById('openPosts');
       const closedPosts = document.getElementById('closedPosts');

       openTab.addEventListener('click', () => {
           openTab.classList.add('text-blue-500', 'border-blue-500');
           openTab.classList.remove('text-gray-500');
           closedTab.classList.remove('text-blue-500', 'border-blue-500');
           closedTab.classList.add('text-gray-500');

           openPosts.classList.remove('hidden');
           closedPosts.classList.add('hidden');
       });

       closedTab.addEventListener('click', () => {
           closedTab.classList.add('text-blue-500', 'border-blue-500');
           closedTab.classList.remove('text-gray-500');
           openTab.classList.remove('text-blue-500', 'border-blue-500');
           openTab.classList.add('text-gray-500');

           closedPosts.classList.remove('hidden');
           openPosts.classList.add('hidden');
       });