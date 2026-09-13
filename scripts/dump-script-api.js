/*
 * Dump the method surface of `base` inside a SeaTable base.
 *
 * The JavaScript reference in docs/javascript/ describes two different APIs
 * (see "Editing the JavaScript reference" in README.md). The scripting half
 * has no machine-readable source, so this script is how you find out what it
 * actually offers.
 *
 * Usage:
 *   1. Open any base -> Scripts -> new JavaScript script
 *   2. Paste this file, run it, read the output panel
 *
 * To check a single method without running the whole dump:
 *   output.text(typeof base.insertColumn);   // "undefined" -> external client only
 */

const methods = new Set();

for (let obj = base; obj && obj !== Object.prototype; obj = Object.getPrototypeOf(obj)) {
    for (const name of Object.getOwnPropertyNames(obj)) {
        try {
            if (typeof base[name] === 'function') methods.add(name);
        } catch (err) {
            // property is a getter that throws -- not a method, skip it
        }
    }
}

output.text([...methods].sort().join('\n'));
output.text('--- base.utils: ' + Object.keys(base.utils || {}).sort().join(', '));
output.text('--- base.context: ' + Object.keys(base.context || {}).sort().join(', '));
