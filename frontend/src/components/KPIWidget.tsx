interface Props {

    title: string;

    value: number;
}

export default function KPIWidget(
    {
        title,
        value
    }: Props
) {

    return (

        <div
            style={{
                border: "1px solid gray",
                padding: "1rem",
                width: "200px"
            }}
        >
            <h3>{title}</h3>

            <h2>{value}</h2>

        </div>
    );
}