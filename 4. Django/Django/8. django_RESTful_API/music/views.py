from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Artist, Music
from .serializers import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer
# Create your views here.

@ api_view(['GET', 'POST'])
def artist_list(request):
    if request.method == 'GET':
        artist = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({f'{serializer.data["name"]} 가수가 생성되었습니다.'}, status=status.HTTP_201_CREATED)



@ api_view(['GET'])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)


@ api_view(['POST'])
def artist_music_list(request, artist_pk):
    artist = Artist.objects.get(pk=artist_pk)

    if request.method == 'POST':
        serializer = MusicListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(artist=artist)
            return Response({f'{serializer.data["title"]} 노래가 생성되었습니다.'}, status=status.HTTP_201_CREATED)


@ api_view(['GET'])
def music_list(request):
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)


@ api_view(['GET', 'PUT', 'DELETE'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    
    if request.method == 'GET':
        serializer = MusicListSerializer(music)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({f'{serializer.data["title"]} 노래로 수정되었습니다.'}, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        music.delete()
        return Response({f'삭제된 노래 id: {music_pk}'}, status=status.HTTP_204_NO_CONTENT)