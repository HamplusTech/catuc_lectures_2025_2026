<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

// Load data
$file = 'data.json';
$data = json_decode(file_get_contents($file), true);

$method = $_SERVER['REQUEST_METHOD'];
$uri = $_SERVER['REQUEST_URI'];

// Extract ID if present (e.g. /api.php?id=2)
$id = isset($_GET['id']) ? intval($_GET['id']) : null;

switch ($method) {
    case 'GET':
        if ($id) {
            // Single user
            $user = array_filter($data, fn($u) => $u['id'] === $id);
            echo json_encode(array_values($user)[0] ?? ["message" => "User not found"]);
        } else {
            // All users
            echo json_encode($data);
        }
        break;

    case 'POST':
        $input = json_decode(file_get_contents('data.json'), true);
        $input['id'] = end($data)['id'] + 1;
        $data[] = $input;
        file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT));
        echo json_encode(["message" => "User added successfully"]);
        break;

    case 'PUT':
        if (!$id) { echo json_encode(["error" => "Missing user ID"]); break; }
        $input = json_decode(file_get_contents('data.json'), true); //php://input
        foreach ($data as &$u) {
            if ($u['id'] === $id) {
                $u = array_merge($u, $input);
                file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT));
                echo json_encode(["message" => "User updated"]);
                exit;
            }
        }
        echo json_encode(["message" => "User not found"]);
        break;

    case 'DELETE':
        if (!$id) { echo json_encode(["error" => "Missing user ID"]); break; }
        $data = array_filter($data, fn($u) => $u['id'] !== $id);
        file_put_contents($file, json_encode(array_values($data), JSON_PRETTY_PRINT));
        echo json_encode(["message" => "User deleted"]);
        break;

    default:
        echo json_encode(["message" => "Unsupported request"]);
        break;
}
