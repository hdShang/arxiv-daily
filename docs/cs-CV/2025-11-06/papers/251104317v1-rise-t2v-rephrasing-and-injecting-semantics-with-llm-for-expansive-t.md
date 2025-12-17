---
layout: default
title: RISE-T2V: Rephrasing and Injecting Semantics with LLM for Expansive Text-to-Video Generation
---

# RISE-T2V: Rephrasing and Injecting Semantics with LLM for Expansive Text-to-Video Generation

**arXiv**: [2511.04317v1](https://arxiv.org/abs/2511.04317) | [PDF](https://arxiv.org/pdf/2511.04317.pdf)

**作者**: Xiangjun Zhang, Litong Gong, Yinglin Zheng, Yansong Liu, Wentao Jiang, Mingyi Xu, Biao Wang, Tiezheng Ge, Ming Zeng

---

## 💡 一句话要点

**提出RISE-T2V框架，通过集成提示重述和语义特征提取，提升文本到视频生成质量。**

**关键词**: `文本到视频生成` `提示重述` `语义特征提取` `扩散模型` `大语言模型集成`

## 📋 核心要点

1. 核心问题：现有文本到视频模型对简洁提示理解不足，导致视频质量下降。
2. 方法要点：引入Rephrasing Adapter，利用LLM隐藏状态作为条件，隐式重述提示。
3. 实验或效果：框架通用，适用于多种视频扩散模型，显著提升视频生成质量。

## 📄 摘要（原文）

> Most text-to-video(T2V) diffusion models depend on pre-trained text encoders
> for semantic alignment, yet they often fail to maintain video quality when
> provided with concise prompts rather than well-designed ones. The primary issue
> lies in their limited textual semantics understanding. Moreover, these text
> encoders cannot rephrase prompts online to better align with user intentions,
> which limits both the scalability and usability of the models, To address these
> challenges, we introduce RISE-T2V, which uniquely integrates the processes of
> prompt rephrasing and semantic feature extraction into a single and seamless
> step instead of two separate steps. RISE-T2V is universal and can be applied to
> various pre-trained LLMs and video diffusion models(VDMs), significantly
> enhancing their capabilities for T2V tasks. We propose an innovative module
> called the Rephrasing Adapter, enabling diffusion models to utilize text hidden
> states during the next token prediction of the LLM as a condition for video
> generation. By employing a Rephrasing Adapter, the video generation model can
> implicitly rephrase basic prompts into more comprehensive representations that
> better match the user's intent. Furthermore, we leverage the powerful
> capabilities of LLMs to enable video generation models to accomplish a broader
> range of T2V tasks. Extensive experiments demonstrate that RISE-T2V is a
> versatile framework applicable to different video diffusion model
> architectures, significantly enhancing the ability of T2V models to generate
> high-quality videos that align with user intent. Visual results are available
> on the webpage at https://rise-t2v.github.io.

