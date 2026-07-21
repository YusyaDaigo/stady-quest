function MenuButton({
  children,
  onClick,
  disabled = false,
  variant = "default",
  wide = false,
}) {
  const classNames = [
    "menu-button",
    `menu-button--${variant}`,
    wide ? "menu-button--wide" : "",
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={classNames}
    >
      {children}
    </button>
  );
}

export default MenuButton;
