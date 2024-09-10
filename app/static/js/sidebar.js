document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-btn');
    const body = document.body;

    toggleBtn.addEventListener('click', function() {
        sidebar.classList.toggle('expanded');
        body.classList.toggle('sidebar-expanded');
    });

    // Cerrar la barra lateral al hacer clic fuera de ella
    document.addEventListener('click', function(event) {
        if (!sidebar.contains(event.target) && !toggleBtn.contains(event.target)) {
            sidebar.classList.remove('expanded');
            body.classList.remove('sidebar-expanded');
        }
    });
}); 