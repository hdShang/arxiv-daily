---
layout: default
title: CloseUpShot: Close-up Novel View Synthesis from Sparse-views via Point-conditioned Diffusion Model
---

# CloseUpShot: Close-up Novel View Synthesis from Sparse-views via Point-conditioned Diffusion Model

**arXiv**: [2511.13121v1](https://arxiv.org/abs/2511.13121) | [PDF](https://arxiv.org/pdf/2511.13121.pdf)

**作者**: Yuqi Zhang, Guanying Chen, Jiaxing Chen, Chuanyu Fu, Chuan Huang, Shuguang Cui

---

## 💡 一句话要点

**提出CloseUpShot框架，通过点条件扩散模型解决稀疏视图下近景新视角合成的挑战**

**关键词**: `新视角合成` `点条件扩散模型` `稀疏视图重建` `遮挡感知噪声抑制` `全局结构引导`

## 📋 核心要点

1. 核心问题：稀疏输入视图在近景场景中难以捕捉细粒度细节，导致重建质量差
2. 方法要点：采用分层扭曲和遮挡感知噪声抑制，结合全局结构引导提升条件图像质量
3. 实验或效果：在多个数据集上优于现有方法，尤其在近景新视角合成中表现突出

## 📄 摘要（原文）

> Reconstructing 3D scenes and synthesizing novel views from sparse input views is a highly challenging task. Recent advances in video diffusion models have demonstrated strong temporal reasoning capabilities, making them a promising tool for enhancing reconstruction quality under sparse-view settings. However, existing approaches are primarily designed for modest viewpoint variations, which struggle in capturing fine-grained details in close-up scenarios since input information is severely limited. In this paper, we present a diffusion-based framework, called CloseUpShot, for close-up novel view synthesis from sparse inputs via point-conditioned video diffusion. Specifically, we observe that pixel-warping conditioning suffers from severe sparsity and background leakage in close-up settings. To address this, we propose hierarchical warping and occlusion-aware noise suppression, enhancing the quality and completeness of the conditioning images for the video diffusion model. Furthermore, we introduce global structure guidance, which leverages a dense fused point cloud to provide consistent geometric context to the diffusion process, to compensate for the lack of globally consistent 3D constraints in sparse conditioning inputs. Extensive experiments on multiple datasets demonstrate that our method outperforms existing approaches, especially in close-up novel view synthesis, clearly validating the effectiveness of our design.

