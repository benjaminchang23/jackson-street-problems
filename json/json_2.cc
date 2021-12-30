#include <iostream>

#include <nlohmann/json.hpp>

using njson = nlohmann::json;

int main()
{
    // create an array using push_back
    njson j;
    j.push_back("foo");
    j.push_back(1);
    j.push_back(true);

    // also use emplace_back
    j.emplace_back(1.78);

    // iterate the array
    for (njson::iterator it = j.begin(); it != j.end(); ++it) {
    std::cout << *it << '\n';
    }

    // range-based for
    for (auto& element : j) {
    std::cout << element << '\n';
    }

    // getter/setter
    const auto tmp = j[0].get<std::string>();
    j[1] = 42;
    bool foo = j.at(2);
    std::cout << "foo at 2?: " << foo << std::endl;

    // comparison
    j == R"(["foo", 1, true, 1.78])"_json;  // true

    // other stuff
    j.size();     // 4 entries
    j.empty();    // false
    j.type();     // json::value_t::array
    j.clear();    // the array is empty again

    // convenience type checkers
    j.is_null();
    j.is_boolean();
    j.is_number();
    j.is_object();
    j.is_array();
    j.is_string();

    // create an object
    njson o;
    o["foo"] = 23;
    o["bar"] = false;
    o["baz"] = 3.141;

    // also use emplace
    o.emplace("weather", "sunny");

    // special iterator member functions for objects
    for (njson::iterator it = o.begin(); it != o.end(); ++it) {
    std::cout << it.key() << " : " << it.value() << "\n";
    }

    // the same code as range for
    for (auto& el : o.items()) {
    std::cout << el.key() << " : " << el.value() << "\n";
    }

    // // even easier with structured bindings (C++17)
    // for (auto& [key, value] : o.items()) {
    // std::cout << key << " : " << value << "\n";
    // }

    // find an entry
    if (o.contains("foo")) {
    // there is an entry with key "foo"
    }

    // or via find and an iterator
    if (o.find("foo") != o.end()) {
    // there is an entry with key "foo"
    }

    // or simpler using count()
    int foo_present = o.count("foo"); // 1
    int fob_present = o.count("fob"); // 0

    std::cout << "foo: " << foo_present << std::endl;
    std::cout << "fob: " << fob_present << std::endl;

    // delete an entry
    o.erase("foo");

    std::cout << j.dump(4) << std::endl;

    return 0;
}