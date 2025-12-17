---
layout: default
title: DINO-Tok: Adapting DINO for Visual Tokenizers
---

# DINO-Tok: Adapting DINO for Visual Tokenizers

**arXiv**: [2511.20565v1](https://arxiv.org/abs/2511.20565) | [PDF](https://arxiv.org/pdf/2511.20565.pdf)

**作者**: Mingkai Jia, Mingxiao Li, Liaoyuan Fan, Tianxing Shi, Jiaxin Guo, Zeming Li, Xiaoyang Guo, Xiao-Xiao Long, Qian Zhang, Ping Tan, Wei Yin

---

## 💡 一句话要点

**提出DINO-Tok视觉分词器，结合浅层与深层特征以改进语义与重建平衡。**

**关键词**: `视觉分词器` `DINO模型` `向量量化` `潜在生成模型` `图像重建` `PCA重加权`

## 📋 核心要点

1. 现有视觉分词器训练困难，难以平衡语义表示与重建保真度。
2. 集成DINO的层次特征，使用全局PCA重加权稳定向量量化。
3. 在ImageNet上实现SOTA重建性能，PSNR达28.54和23.98。

## 📄 摘要（原文）

> Recent advances in visual generation have highlighted the rise of Latent Generative Models (LGMs), which rely on effective visual tokenizers to bridge pixels and semantics. However, existing tokenizers are typically trained from scratch and struggle to balance semantic representation and reconstruction fidelity, particularly in high-dimensional latent spaces. In this work, we introduce DINO-Tok, a DINO-based visual tokenizer that unifies hierarchical representations into an information-complete latent space. By integrating shallow features that retain fine-grained details with deep features encoding global semantics, DINO-Tok effectively bridges pretrained representations and visual generation. We further analyze the challenges of vector quantization (VQ) in this high-dimensional space, where key information is often lost and codebook collapse occurs. We thus propose a global PCA reweighting mechanism to stabilize VQ and preserve essential information across dimensions. On ImageNet 256$\times$256, DINO-Tok achieves state-of-the-art reconstruction performance, reaching 28.54 PSNR for autoencoding and 23.98 PSNR for VQ-based modeling, significantly outperforming prior tokenizers and comparable to billion-level data trained models (such as Hunyuan and Wan). These results demonstrate that adapting powerful pretrained vision models like DINO for tokenization enables semantically aligned and high-fidelity latent representations, enabling next-generation visual generative models. Code will be publicly available at https://github.com/MKJia/DINO-Tok.

