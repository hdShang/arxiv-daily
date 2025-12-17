---
layout: default
title: LatentPrintFormer: A Hybrid CNN-Transformer with Spatial Attention for Latent Fingerprint identification
---

# LatentPrintFormer: A Hybrid CNN-Transformer with Spatial Attention for Latent Fingerprint identification

**arXiv**: [2511.08119v1](https://arxiv.org/abs/2511.08119) | [PDF](https://arxiv.org/pdf/2511.08119.pdf)

**作者**: Arnab Maity, Manasa, Pavan Kumar C, Raghavendra Ramachandra

---

## 💡 一句话要点

**提出LatentPrintFormer混合模型以解决潜指纹识别中的图像质量低和噪声问题**

**关键词**: `潜指纹识别` `混合模型` `空间注意力` `特征融合` `余弦相似度匹配`

## 📋 核心要点

1. 潜指纹识别面临图像质量低、背景噪声和部分印记等挑战
2. 结合CNN和Transformer提取局部与全局特征，并使用空间注意力模块增强脊线区域
3. 在公开数据集上实验，识别率优于现有方法，尤其在Rank-10表现突出

## 📄 摘要（原文）

> Latent fingerprint identification remains a challenging task due to low image quality, background noise, and partial impressions. In this work, we propose a novel identification approach called LatentPrintFormer. The proposed model integrates a CNN backbone (EfficientNet-B0) and a Transformer backbone (Swin Tiny) to extract both local and global features from latent fingerprints. A spatial attention module is employed to emphasize high-quality ridge regions while suppressing background noise. The extracted features are fused and projected into a unified 512-dimensional embedding, and matching is performed using cosine similarity in a closed-set identification setting. Extensive experiments on two publicly available datasets demonstrate that LatentPrintFormer consistently outperforms three state-of-the-art latent fingerprint recognition techniques, achieving higher identification rates across Rank-10.

