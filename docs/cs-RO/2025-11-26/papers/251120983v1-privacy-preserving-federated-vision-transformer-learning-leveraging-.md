---
layout: default
title: Privacy-Preserving Federated Vision Transformer Learning Leveraging Lightweight Homomorphic Encryption in Medical AI
---

# Privacy-Preserving Federated Vision Transformer Learning Leveraging Lightweight Homomorphic Encryption in Medical AI

**arXiv**: [2511.20983v1](https://arxiv.org/abs/2511.20983) | [PDF](https://arxiv.org/pdf/2511.20983.pdf)

**作者**: Al Amin, Kamrul Hasan, Liang Hong, Sharif Ullah

---

## 💡 一句话要点

**提出结合视觉Transformer与同态加密的联邦学习框架，以保护医疗AI中的隐私。**

**关键词**: `联邦学习` `视觉Transformer` `同态加密` `医疗AI` `隐私保护` `图像分类`

## 📋 核心要点

1. 医疗联邦学习中梯度易受重建攻击，泄露敏感信息。
2. 使用ViT CLS令牌加密聚合，减少通信并增强隐私。
3. 实验显示加密方法防止攻击，保持高分类准确率。

## 📄 摘要（原文）

> Collaborative machine learning across healthcare institutions promises improved diagnostic accuracy by leveraging diverse datasets, yet privacy regulations such as HIPAA prohibit direct patient data sharing. While federated learning (FL) enables decentralized training without raw data exchange, recent studies show that model gradients in conventional FL remain vulnerable to reconstruction attacks, potentially exposing sensitive medical information. This paper presents a privacy-preserving federated learning framework combining Vision Transformers (ViT) with homomorphic encryption (HE) for secure multi-institutional histopathology classification. The approach leverages the ViT CLS token as a compact 768-dimensional feature representation for secure aggregation, encrypting these tokens using CKKS homomorphic encryption before transmission to the server. We demonstrate that encrypting CLS tokens achieves a 30-fold communication reduction compared to gradient encryption while maintaining strong privacy guarantees. Through evaluation on a three-client federated setup for lung cancer histopathology classification, we show that gradients are highly susceptible to model inversion attacks (PSNR: 52.26 dB, SSIM: 0.999, NMI: 0.741), enabling near-perfect image reconstruction. In contrast, the proposed CLS-protected HE approach prevents such attacks while enabling encrypted inference directly on ciphertexts, requiring only 326 KB of encrypted data transmission per aggregation round. The framework achieves 96.12 percent global classification accuracy in the unencrypted domain and 90.02 percent in the encrypted domain.

