<?php

/**
 * Embedded Google Calendar customization wrapper script
 *
 * Applies a custom color scheme to an embedded Google Calendar.
 *
 * Usage:
 *
 *     Replace standard Google Calendar embedding code, e.g.:
 *
 * <iframe src="http://www.google.com/calendar/embed?src=..."></iframe>
 *
 *     with a reference to this script:
 *
 * <iframe src="gcalendar-wrapper.php?src=..."></iframe>
 *
 * @author      Chris Dornfeld <dornfeld (at) unitz.com>
 * @version     $Id: gcalendar-wrapper.php 1405 2010-05-17 02:23:46Z dornfeld $
 * @link        http://www.unitz.com/gcalendar-wrapper/
 */

/**
 * Set your color scheme below
 */
$calColorBgDark      = '#c3d9ff';	// dark background color
$calColorTextOnDark  = '#000000';	// text appearing on top of dark bg color
$calColorBgLight     = '#e8eef7';	// light background color
$calColorTextOnLight = '#000000';	// text appearing on top of light bg color
$calColorBgToday     = '#ffffcc';	// background color for "today" box

/**
 * Orange color scheme
 */
/*
$calColorBgDark      = '#ffa200';
$calColorTextOnDark  = '#ffffff';
$calColorBgLight     = '#ffeccb';
$calColorTextOnLight = '#000000';
$calColorBgToday     = '#fef0ff';
*/

/**
 * Purple color scheme
 */
/*
$calColorBgDark      = '#4b53a1';
$calColorTextOnDark  = '#ffffff';
$calColorBgLight     = '#d0cfff';
$calColorTextOnLight = '#000000';
$calColorBgToday     = '#fff2cf';
*/

/**
 * Green color scheme
 */
/*
$calColorBgDark      = '#336633';
$calColorTextOnDark  = '#ffffff';
$calColorBgLight     = '#ace0ac';
$calColorTextOnLight = '#003300';
$calColorBgToday     = '#ffe5ac';
*/

/**
 * Google Calendar default color scheme (simplified)
 */
/*
$calColorBgDark      = '#c3d9ff';
$calColorTextOnDark  = '#000000';
$calColorBgLight     = '#e8eef7';
$calColorTextOnLight = '#000000';
$calColorBgToday     = '#ffffcc';
*/

/**
 * For normal use, no changes are needed below this line
 */

define('GOOGLE_CALENDAR_BASE', 'http://www.google.com/');
define('GOOGLE_CALENDAR_EMBED_URL', GOOGLE_CALENDAR_BASE . 'calendar/embed');

/**
 * Prepare stylesheet customizations
 */

$calCustomStyle =<<<EOT

/* misc interface */
.cc-titlebar {
	background-color: {$calColorBgLight} !important;
}
.date-picker-arrow-on,
.drag-lasso,
.agenda-scrollboxBoundary {
	background-color: {$calColorBgDark} !important;
}
td#timezone {
	color: {$calColorTextOnDark} !important;
}

/* tabs */
td#calendarTabs1 div.ui-rtsr-selected,
div.view-cap,
div.view-container-border {
	background-color: {$calColorBgDark} !important;
}
td#calendarTabs1 div.ui-rtsr-selected {
	color: {$calColorTextOnDark} !important;
}
td#calendarTabs1 div.ui-rtsr-unselected {
	background-color: {$calColorBgLight} !important;
	color: {$calColorTextOnLight} !important;
}

/* week view */
table.wk-weektop,
th.wk-dummyth {
	/* days of the week */
	background-color: {$calColorBgDark} !important;
}
div.wk-dayname {
	color: {$calColorTextOnDark} !important;
}
div.wk-today {
	background-color: {$calColorBgLight} !important;
	border: 1px solid #EEEEEE !important;
	color: {$calColorTextOnLight} !important;
}
td.wk-allday {
	background-color: #EEEEEE !important;
}
td.tg-times {
	background-color: {$calColorBgLight} !important;
	color: {$calColorTextOnLight} !important;
}
div.tg-today {
	background-color: {$calColorBgToday} !important;
}

/* month view */
table.mv-daynames-table {
	background-color: {$calColorBgDark} !important;
	/* days of the week */
	color: {$calColorTextOnDark} !important;
}
td.st-bg,
td.st-dtitle {
	/* cell borders */
	border-left: 1px solid {$calColorBgDark} !important;
}
td.st-dtitle {
	/* days of the month */
	background-color: {$calColorBgLight} !important;
	color: {$calColorTextOnLight} !important;
	/* cell borders */
	border-top: 1px solid {$calColorBgDark} !important;
}
td.st-bg-today {
	background-color: {$calColorBgToday} !important;
}

/* agenda view */
div.scrollbox {
	border-top: 1px solid {$calColorBgDark} !important;
	border-left: 1px solid {$calColorBgDark} !important;
}
div.underflow-top {
	border-bottom: 1px solid {$calColorBgDark} !important;
}
div.date-label {
	background-color: {$calColorBgLight} !important;
	color: {$calColorTextOnLight} !important;
}
div.event {
	border-top: 1px solid {$calColorBgDark} !important;
}
div.day {
	border-bottom: 1px solid {$calColorBgDark} !important;
}

EOT;

$calCustomStyle = '<style type="text/css">'.$calCustomStyle.'</style>';

/**
 * Construct calendar URL
 */

$calQuery = '';
if (isset($_SERVER['QUERY_STRING'])) {
	$calQuery = $_SERVER['QUERY_STRING'];
} else if (isset($HTTP_SERVER_VARS['QUERY_STRING'])) {
	$calQuery = $HTTP_SERVER_VARS['QUERY_STRING'];
}
$calUrl = GOOGLE_CALENDAR_EMBED_URL.'?'.$calQuery;

/**
 * Retrieve calendar embedding code
 */

$calRaw = '';
if (in_array('curl', get_loaded_extensions())) {
	$curlObj = curl_init();
	curl_setopt($curlObj, CURLOPT_URL, $calUrl);
	curl_setopt($curlObj, CURLOPT_RETURNTRANSFER, 1);
	if (function_exists('curl_version')) {
		$curlVer = curl_version();
		if (is_array($curlVer) && !empty($curlVer['version']) &&
			version_compare($curlVer['version'], '7.15.2', '>=') &&
			!ini_get('open_basedir') && !ini_get('safe_mode')) {
			// enable HTTP redirect following for cURL:
			// - CURLOPT_FOLLOWLOCATION is disabled when PHP is in safe mode
			// - cURL versions before 7.15.2 had a bug that lumped
			//   redirected page content with HTTP headers
			// http://simplepie.org/support/viewtopic.php?id=1004
			curl_setopt($curlObj, CURLOPT_FOLLOWLOCATION, 1);
			curl_setopt($curlObj, CURLOPT_MAXREDIRS, 5);
		}
	}
	$calRaw = curl_exec($curlObj);
	curl_close($curlObj);
} else if (ini_get('allow_url_fopen')) {
	// fopen should follow HTTP redirects in recent versions
	$fp = fopen($calUrl, 'r');
	while (!feof($fp)) {
		$calRaw .= fread($fp, 8192);
	}
	fclose($fp);
} else {
	trigger_error("Can't use cURL or fopen to retrieve Google Calendar", E_USER_ERROR);
}

/**
 * Insert BASE tag to accommodate relative paths
 */

$titleTag = '<title>';
$baseTag = '<base href="'.GOOGLE_CALENDAR_EMBED_URL.'">';
$calCustomized = preg_replace("/".preg_quote($titleTag,'/')."/i", $baseTag.$titleTag, $calRaw);

/**
 * Insert custom styles
 */

$headEndTag = '</head>';
$calCustomized = preg_replace("/".preg_quote($headEndTag,'/')."/i", $calCustomStyle.$headEndTag, $calCustomized);

/**
 * Extract and modify calendar setup data
 */

$calSettingsPattern = "(\{\s*window\._init\(\s*)(\{.+\})(\s*\)\;\s*\})";

if (preg_match("/$calSettingsPattern/", $calCustomized, $matches)) {
	$calSettingsJson = $matches[2];

	$pearJson = null;
	if (!function_exists('json_encode')) {
		// no built-in JSON support, attempt to use PEAR::Services_JSON library
		if (!class_exists('Services_JSON')) {
			require_once('Services/JSON.php');
		}
		$pearJson = new Services_JSON();
	}

	if (function_exists('json_decode')) {
		$calSettings = json_decode($calSettingsJson);
	} else {
		$calSettings = $pearJson->decode($calSettingsJson);
	}

	// set base URL to accommodate relative paths
	$calSettings->baseUrl = GOOGLE_CALENDAR_BASE;

	// splice in updated calendar setup data
	if (function_exists('json_encode')) {
		$calSettingsJson = json_encode($calSettings);
	} else {
		$calSettingsJson = $pearJson->encode($calSettings);
	}
	// prevent unwanted variable substitutions within JSON data
	// preg_quote() results in excessive escaping
	$calSettingsJson = str_replace('$', '\\$', $calSettingsJson);
	$calCustomized = preg_replace("/$calSettingsPattern/", "\\1$calSettingsJson\\3", $calCustomized);
}

/**
 * Show output
 */

header('Content-type: text/html');
print $calCustomized;
