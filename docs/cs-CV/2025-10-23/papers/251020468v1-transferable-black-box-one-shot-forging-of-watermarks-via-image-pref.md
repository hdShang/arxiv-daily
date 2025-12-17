---
layout: default
title: Transferable Black-Box One-Shot Forging of Watermarks via Image Preference Models
---

# Transferable Black-Box One-Shot Forging of Watermarks via Image Preference Models

**arXiv**: [2510.20468v1](https://arxiv.org/abs/2510.20468) | [PDF](https://arxiv.org/pdf/2510.20468.pdf)

**作者**: Tomáš Souček, Sylvestre-Alvise Rebuffi, Pierre Fernandez, Nikola Jovanović, Hady Elsahar, Valeriu Lacatusu, Tuan Tran, Alexandre Mourachko

---

## 💡 一句话要点

**提出基于偏好模型的黑盒一次性水印伪造方法，质疑后处理水印安全性**

**关键词**: `水印伪造` `偏好模型` `黑盒攻击` `图像优化` `后处理水印`

## 📋 核心要点

1. 核心问题：后处理图像水印的伪造攻击研究不足，威胁内容认证
2. 方法要点：训练偏好模型评估水印，通过反向传播优化图像实现伪造
3. 实验或效果：在多种水印模型上验证伪造有效性，无需水印模型知识

## 📄 摘要（原文）

> Recent years have seen a surge in interest in digital content watermarking
> techniques, driven by the proliferation of generative models and increased
> legal pressure. With an ever-growing percentage of AI-generated content
> available online, watermarking plays an increasingly important role in ensuring
> content authenticity and attribution at scale. There have been many works
> assessing the robustness of watermarking to removal attacks, yet, watermark
> forging, the scenario when a watermark is stolen from genuine content and
> applied to malicious content, remains underexplored. In this work, we
> investigate watermark forging in the context of widely used post-hoc image
> watermarking. Our contributions are as follows. First, we introduce a
> preference model to assess whether an image is watermarked. The model is
> trained using a ranking loss on purely procedurally generated images without
> any need for real watermarks. Second, we demonstrate the model's capability to
> remove and forge watermarks by optimizing the input image through
> backpropagation. This technique requires only a single watermarked image and
> works without knowledge of the watermarking model, making our attack much
> simpler and more practical than attacks introduced in related work. Third, we
> evaluate our proposed method on a variety of post-hoc image watermarking
> models, demonstrating that our approach can effectively forge watermarks,
> questioning the security of current watermarking approaches. Our code and
> further resources are publicly available.

