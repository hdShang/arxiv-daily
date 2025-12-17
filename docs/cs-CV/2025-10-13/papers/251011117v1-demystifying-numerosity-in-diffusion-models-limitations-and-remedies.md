---
layout: default
title: Demystifying Numerosity in Diffusion Models -- Limitations and Remedies
---

# Demystifying Numerosity in Diffusion Models -- Limitations and Remedies

**arXiv**: [2510.11117v1](https://arxiv.org/abs/2510.11117) | [PDF](https://arxiv.org/pdf/2510.11117.pdf)

**作者**: Yaqi Zhao, Xiaochen Wang, Li Dong, Wentao Zhang, Yuhui Yuan

---

## 💡 一句话要点

**提出注入计数感知布局信息的方法，以解决扩散模型在文本提示中计数准确性不足的问题。**

**关键词**: `扩散模型` `计数准确性` `噪声先验` `布局信息注入` `文本到图像生成`

## 📋 核心要点

1. 核心问题：扩散模型难以准确生成文本提示中指定的对象数量，仅靠扩大模型和数据集无效。
2. 方法要点：通过向噪声先验注入计数感知布局信息，控制对象数量生成。
3. 实验或效果：在基准测试中，准确率从20.0%提升至85.3%，并实现跨场景泛化。

## 📄 摘要（原文）

> Numerosity remains a challenge for state-of-the-art text-to-image generation
> models like FLUX and GPT-4o, which often fail to accurately follow counting
> instructions in text prompts. In this paper, we aim to study a fundamental yet
> often overlooked question: Can diffusion models inherently generate the correct
> number of objects specified by a textual prompt simply by scaling up the
> dataset and model size? To enable rigorous and reproducible evaluation, we
> construct a clean synthetic numerosity benchmark comprising two complementary
> datasets: GrayCount250 for controlled scaling studies, and NaturalCount6
> featuring complex naturalistic scenes. Second, we empirically show that the
> scaling hypothesis does not hold: larger models and datasets alone fail to
> improve counting accuracy on our benchmark. Our analysis identifies a key
> reason: diffusion models tend to rely heavily on the noise initialization
> rather than the explicit numerosity specified in the prompt. We observe that
> noise priors exhibit biases toward specific object counts. In addition, we
> propose an effective strategy for controlling numerosity by injecting
> count-aware layout information into the noise prior. Our method achieves
> significant gains, improving accuracy on GrayCount250 from 20.0\% to 85.3\% and
> on NaturalCount6 from 74.8\% to 86.3\%, demonstrating effective generalization
> across settings.

