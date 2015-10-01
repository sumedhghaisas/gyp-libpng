#include <iostream>
#include <string>

#include <node.h>
#include <v8.h>

using namespace std;
using namespace v8;

extern "C" int libpng_test(int argc, char* argv[]);

void libpng_test_wrap(const FunctionCallbackInfo<v8::Value>& args)
{
    v8::Isolate* isolate;
    isolate = args.GetIsolate();

    int argc = 2;
    char* argv[] = {"png_test", "pngtest.png"};

    int status = libpng_test(argc, argv);
    Local<Number> out = Number::New(isolate, status);
    args.GetReturnValue().Set(out);
}

void init(Handle<Object> exports)
{
  Isolate* isolate = v8::Isolate::GetCurrent();
  exports->Set(String::NewFromUtf8(isolate, "pngTest", v8::String::kInternalizedString),
      FunctionTemplate::New(isolate, libpng_test_wrap)->GetFunction());
}

NODE_MODULE(png_test, init)
