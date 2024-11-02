interface Props {
  onClick?: () => null;
  text: string;
}

const Button = ({ ...props }: Props) => {
  return (
    <button className="text-indigo-600 bg-white px-2 py-1 rounded">
      {props.text}
    </button>
  );
};

export default Button;
