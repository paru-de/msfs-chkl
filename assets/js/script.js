// Toggle category collapse/expand
function toggleCategory(element) {
  const category = element.parentElement;
  const checklistItems = category.querySelector('.checklist-items');
  const icon = element.querySelector('i');

  checklistItems.classList.toggle('collapsed');
  icon.classList.toggle('fa-chevron-down');
  icon.classList.toggle('fa-chevron-up');
}

// Toggle checklist collapse/expand and mark as completed
function toggleChecklist(element) {
  const checklist = element.parentElement;
  const checklistContent = checklist.querySelector('.checklist-content');
  const icon = element.querySelector('.checklist-icon');

  // Calculate the natural height of the content
  if (checklistContent.classList.contains('collapsed')) {
    // Expand the content
    checklistContent.style.maxHeight = checklistContent.scrollHeight + 'px';
    checklistContent.classList.remove('collapsed');
    icon.classList.remove('fa-chevron-down');
    icon.classList.add('fa-chevron-up');
    checklist.classList.remove('completed');
  } else {
    // Collapse the content
    checklistContent.style.maxHeight = '0';
    checklistContent.classList.add('collapsed');
    icon.classList.remove('fa-chevron-up');
    icon.classList.add('fa-chevron-down');
    checklist.classList.add('completed');
  }
}

// Index menu
document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.checklist-content').forEach(item => {
    item.classList.remove('collapsed');
    item.style.maxHeight = item.scrollHeight + 'px';
  });

  document.querySelectorAll('.checklist-icon').forEach(icon => {
    icon.classList.add('fa-chevron-up');
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.scroll-container');
  const btn = container.querySelector('.scroll-btn');
  const menu = container.querySelector('.scroll-menu ul');
  const titles = [...document.querySelectorAll('.checklist-title')];

  titles.forEach((title, i) => {
    const li = document.createElement('li');
    li.textContent = title.textContent.trim() || `Section ${i + 1}`;
    li.addEventListener('click', e => {
      e.stopPropagation();
      window.scrollTo({
        top: title.offsetTop - 30,
        behavior: 'smooth',
      });
      menu.parentElement.classList.remove('open');
    });
    menu.appendChild(li);
  });

  btn.addEventListener('click', e => {
    e.stopPropagation();
    container.querySelector('.scroll-menu').classList.toggle('open');
  });

  document.addEventListener('click', () => {
    container.querySelector('.scroll-menu').classList.remove('open');
  });
});
