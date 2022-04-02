const path = require('path');
var webpack = require("webpack");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
    mode: 'development',
    entry: ["./assets/js/main.js", "./assets/scss/main.scss"],
    output: {
        filename: "js/main.js",
        path: path.resolve(__dirname, 'static/core/'),
        clean: true,
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }),
        new MiniCssExtractPlugin({
            filename: "css/main.css",
        }),
        // new CopyPlugin({
        //     patterns: [
        //         { from: "./assets/images", to: "images" },
        //     ],
        // }),
    ],
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    },
                    {
                        loader: 'css-loader',
                        options: {
                            url: false,
                        }
                    },
                    'sass-loader'
                ]
            },

        ]
    }
};