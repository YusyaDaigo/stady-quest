function MenuSection({
  title,
  description,
  children,
  grid = false,
}) {
  return (
    <section className="menu-section">
      <h3 className="menu-section__title">
        {title}
      </h3>

      {description && (
        <p className="menu-section__description">
          {description}
        </p>
      )}

      <div
        className={
          grid
            ? "menu-section__content menu-section__content--grid"
            : "menu-section__content"
        }
      >
        {children}
      </div>
    </section>
  );
}

export default MenuSection;
