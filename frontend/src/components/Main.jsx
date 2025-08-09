import IDBox from "./IDBox";
import "./Main.css";

export default function Main() {
	return (
		<main className="main">
			<h1 className="title">snowplow</h1>
			<p className="description">
				Snowplow generates an unique, time-sortable ID using Twitter's Snowflake
				technique.
			</p>
			<IDBox />
		</main>
	);
}
