-- Hello World in Lua
print("Hello, World!")

-- local grpc = require("grpc")


local ffi = require("ffi")
ffi.cdef[[
   // Add gRPC C definitions here
]]
local grpc = ffi.load("grpc")
-- Use grpc API here