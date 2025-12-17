---
layout: default
title: Versatile and Efficient Medical Image Super-Resolution Via Frequency-Gated Mamba
---

# Versatile and Efficient Medical Image Super-Resolution Via Frequency-Gated Mamba

**arXiv**: [2510.27296v1](https://arxiv.org/abs/2510.27296) | [PDF](https://arxiv.org/pdf/2510.27296.pdf)

**作者**: Wenfeng Huang, Xiangyun Liao, Wei Cao, Wenjing Jia, Weixin Si

---

## 💡 一句话要点

**提出FGMamba以高效增强医学图像超分辨率，结合频率感知状态空间建模**

**关键词**: `医学图像超分辨率` `状态空间模型` `频率感知` `轻量架构` `多模态评估`

## 📋 核心要点

1. 医学图像超分辨率需平衡长程结构建模与细粒度频率细节，计算开销大
2. 引入GASM模块集成状态空间建模与注意力，PFFM模块通过FFT融合多分辨率高频细节
3. 在五种医学影像模态上验证，PSNR/SSIM优于SOTA，参数少于0.75M

## 📄 摘要（原文）

> Medical image super-resolution (SR) is essential for enhancing diagnostic
> accuracy while reducing acquisition cost and scanning time. However, modeling
> both long-range anatomical structures and fine-grained frequency details with
> low computational overhead remains challenging. We propose FGMamba, a novel
> frequency-aware gated state-space model that unifies global dependency modeling
> and fine-detail enhancement into a lightweight architecture. Our method
> introduces two key innovations: a Gated Attention-enhanced State-Space Module
> (GASM) that integrates efficient state-space modeling with dual-branch spatial
> and channel attention, and a Pyramid Frequency Fusion Module (PFFM) that
> captures high-frequency details across multiple resolutions via FFT-guided
> fusion. Extensive evaluations across five medical imaging modalities
> (Ultrasound, OCT, MRI, CT, and Endoscopic) demonstrate that FGMamba achieves
> superior PSNR/SSIM while maintaining a compact parameter footprint ($<$0.75M),
> outperforming CNN-based and Transformer-based SOTAs. Our results validate the
> effectiveness of frequency-aware state-space modeling for scalable and accurate
> medical image enhancement.

