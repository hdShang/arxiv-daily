---
layout: default
title: VIST3A: Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator
---

# VIST3A: Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator

**arXiv**: [2510.13454v1](https://arxiv.org/abs/2510.13454) | [PDF](https://arxiv.org/pdf/2510.13454.pdf)

**作者**: Hyojun Go, Dominik Narnhofer, Goutam Bhat, Prune Truong, Federico Tombari, Konrad Schindler

---

## 💡 一句话要点

**提出VIST3A框架，通过缝合文本到视频生成器与3D重建网络实现文本到3D生成**

**关键词**: `文本到3D生成` `模型缝合` `3D重建` `视频生成` `直接奖励微调`

## 📋 核心要点

1. 核心问题：结合文本到视频生成与3D重建模型，以生成一致且感知可信的3D场景
2. 方法要点：使用模型缝合技术连接组件，并通过直接奖励微调对齐生成器与解码器
3. 实验或效果：评估显示优于先前的文本到3D模型，并支持高质量文本到点云生成

## 📄 摘要（原文）

> The rapid progress of large, pretrained models for both visual content
> generation and 3D reconstruction opens up new possibilities for text-to-3D
> generation. Intuitively, one could obtain a formidable 3D scene generator if
> one were able to combine the power of a modern latent text-to-video model as
> "generator" with the geometric abilities of a recent (feedforward) 3D
> reconstruction system as "decoder". We introduce VIST3A, a general framework
> that does just that, addressing two main challenges. First, the two components
> must be joined in a way that preserves the rich knowledge encoded in their
> weights. We revisit model stitching, i.e., we identify the layer in the 3D
> decoder that best matches the latent representation produced by the
> text-to-video generator and stitch the two parts together. That operation
> requires only a small dataset and no labels. Second, the text-to-video
> generator must be aligned with the stitched 3D decoder, to ensure that the
> generated latents are decodable into consistent, perceptually convincing 3D
> scene geometry. To that end, we adapt direct reward finetuning, a popular
> technique for human preference alignment. We evaluate the proposed VIST3A
> approach with different video generators and 3D reconstruction models. All
> tested pairings markedly improve over prior text-to-3D models that output
> Gaussian splats. Moreover, by choosing a suitable 3D base model, VIST3A also
> enables high-quality text-to-pointmap generation.

