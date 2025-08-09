import { useState } from "react";
import axios from "axios";
import "./IDBox.css";

export default function IDBox() {
	const [snowflake, setSnowflake] = useState("");
	const [loading, setLoading] = useState(false);

	const getId = async () => {
		setLoading(true);
		const apiUrl = import.meta.env.VITE_API_URL;
		try {
			const response = await axios.get(`${apiUrl}`);
			const data = response.data;
			setSnowflake(data.id);
		} catch (error) {
			console.error(error);
			setSnowflake("");
		} finally {
			setLoading(false);
		}
	};

	return (
		<>
			<div className="id-generator">
				<input
					type="text"
					className="id-box"
					value={snowflake ?? ""}
					readOnly
					placeholder="Click to generate an ID..."
				/>
				<button onClick={getId} disabled={loading} className="generate-button">
					{loading ? "Generating..." : "Generate"}
				</button>
			</div>
		</>
	);
}
