'use strict';
var libpng = require('./build/Release/png_test');
var expect = require('chai').expect;

describe('functionality', function() {

    describe('png_test', function() {

        it('should be able to process .png file', function() {
            var result = libpng.pngTest();
            expect(result).to.eql(0);
        });
    });
});
