
#include <math.h>
#include "raylib.h"
#include <stdio.h>


int isSelected(Vector2 position, Vector2 mousePosition, float objectRadius);

int main(void)
{

    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "Raylib");

    Camera2D camera = { 0 };
    camera.offset = (Vector2){ screenHeight/2.0f, screenWidth/2.0f }; 
    Vector2 ballPosition = {screenHeight/2.0f, screenHeight/2.0f};
    camera.zoom = 1.0f;


    SetTargetFPS(60);       

    while (!WindowShouldClose())   {

        float wheel = GetMouseWheelMove();
        if (wheel != 0){
            camera.zoom += wheel * 0.1f;
            if (camera.zoom < 0.1f) camera.zoom = 0.1f;
        }

        if (IsKeyDown(KEY_D)) camera.offset.x += 2.0f;
        if (IsKeyDown(KEY_A)) camera.offset.x -= 2.0f;
        if (IsKeyDown(KEY_W)) camera.offset.y -= 2.0f;
        if (IsKeyDown(KEY_S)) camera.offset.y += 2.0f;

        Vector2 worldMouse = GetScreenToWorld2D(GetMousePosition(), camera);
        if (IsMouseButtonDown(MOUSE_BUTTON_LEFT) && isSelected(ballPosition, worldMouse, 50)) {
            ballPosition = worldMouse;
        }

        BeginDrawing();
            ClearBackground(RAYWHITE);
            BeginMode2D(camera);
                DrawCircleV(ballPosition, 50, MAROON);
            EndMode2D();
        EndDrawing();

        }

    CloseWindow();

    return 0;
}


int isSelected(Vector2 position, Vector2 mousePosition, float objectRadius){

    Vector2 hypotenuse = {position.x - mousePosition.x, position.y - mousePosition.y};
    float distance = hypot(hypotenuse.x, hypotenuse.y);

    if (distance <= objectRadius){
        return 1;
    }else {
        return 0;
    }

}