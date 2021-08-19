const { src, dest, watch, series } = require("gulp");
const rename = require("gulp-rename");
const uglify = require("gulp-uglify");
const cleanCSS = require("gulp-clean-css");

const minifyJs = () =>
    src('website/static/js/*.js')
    .pipe(uglify())
    .pipe(rename({
        extname: '.min.js'
    }))
    .pipe(dest('website/static/dest_js/'));

const minifyCss = () =>
    src('website/static/style/*.css')
    .pipe(cleanCSS())
    .pipe(rename({
        extname: '.min.css'
    }))
    .pipe(dest('website/static/dest_style/'));

const watchJsFiles = () => watch('website/static/js/*.js', minifyJs());
const watchCssFiles = () => watch('website/static/style/*.css', minifyCss());

exports.default = function (){
    watchJsFiles();
    watchCssFiles();
}