---
layout: default
title: DialectGen: Benchmarking and Improving Dialect Robustness in Multimodal Generation
---

# DialectGen: Benchmarking and Improving Dialect Robustness in Multimodal Generation

**arXiv**: [2510.14949v1](https://arxiv.org/abs/2510.14949) | [PDF](https://arxiv.org/pdf/2510.14949.pdf)

**作者**: Yu Zhou, Sohyun An, Haikang Deng, Da Yin, Clark Peng, Cho-Jui Hsieh, Kai-Wei Chang, Nanyun Peng

---

## 💡 一句话要点

**提出编码器方法以提升多模态生成模型对英语方言的鲁棒性**

**关键词**: `多模态生成` `方言鲁棒性` `编码器方法` `基准测试` `性能优化`

## 📋 核心要点

1. 核心问题：多模态生成模型在方言文本输入下性能显著下降，降幅达32.26%至48.17%
2. 方法要点：设计编码器策略，使模型识别新方言特征并保持标准英语性能
3. 实验或效果：在Stable Diffusion 1.5等模型上，方言性能提升34.4%，标准英语性能几乎无损

## 📄 摘要（原文）

> Contact languages like English exhibit rich regional variations in the form
> of dialects, which are often used by dialect speakers interacting with
> generative models. However, can multimodal generative models effectively
> produce content given dialectal textual input? In this work, we study this
> question by constructing a new large-scale benchmark spanning six common
> English dialects. We work with dialect speakers to collect and verify over 4200
> unique prompts and evaluate on 17 image and video generative models. Our
> automatic and human evaluation results show that current state-of-the-art
> multimodal generative models exhibit 32.26% to 48.17% performance degradation
> when a single dialect word is used in the prompt. Common mitigation methods
> such as fine-tuning and prompt rewriting can only improve dialect performance
> by small margins (< 7%), while potentially incurring significant performance
> degradation in Standard American English (SAE). To this end, we design a
> general encoder-based mitigation strategy for multimodal generative models. Our
> method teaches the model to recognize new dialect features while preserving SAE
> performance. Experiments on models such as Stable Diffusion 1.5 show that our
> method is able to simultaneously raise performance on five dialects to be on
> par with SAE (+34.4%), while incurring near zero cost to SAE performance.

