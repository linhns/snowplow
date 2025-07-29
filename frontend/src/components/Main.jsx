import { useState } from "react";
import "./Main.css";
import axios from "axios";

export default function Main() {
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
		<main>
			<h1>Generate a unique ID</h1>
			<p className="description">
				Snowplow generates an unique, time-sortable ID using Twitter's Snowflake
				technique.
			</p>
			<div className="id-generator">
				<input
					type="text"
					className="id-field"
					value={snowflake ?? ""}
					readOnly
					placeholder="Click to generate an ID..."
				/>
				<button onClick={getId} disabled={loading}>
					{loading ? "Generating..." : "Generate"}
				</button>
			</div>
		</main>
	);
}
