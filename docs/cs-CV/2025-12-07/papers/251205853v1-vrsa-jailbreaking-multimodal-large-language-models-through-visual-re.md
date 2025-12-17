---
layout: default
title: VRSA: Jailbreaking Multimodal Large Language Models through Visual Reasoning Sequential Attack
---

# VRSA: Jailbreaking Multimodal Large Language Models through Visual Reasoning Sequential Attack

**arXiv**: [2512.05853v1](https://arxiv.org/abs/2512.05853) | [PDF](https://arxiv.org/pdf/2512.05853.pdf)

**作者**: Shiji Zhao, Shukun Xiong, Yao Huang, Yan Jin, Zhenyu Wu, Jiyang Guan, Ranjie Duan, Jialing Tao, Hui Xue, Xingxing Wei

---

## 💡 一句话要点

**提出视觉推理序列攻击以评估多模态大语言模型在视觉模态中的安全风险**

**关键词**: `多模态大语言模型` `视觉推理攻击` `越狱攻击` `安全评估` `序列图像生成`

## 📋 核心要点

1. 核心问题：多模态大语言模型在视觉模态中的推理安全风险被忽视，易被用于越狱攻击。
2. 方法要点：通过分解有害文本为序列相关子图像，结合自适应场景优化和语义连贯补全，诱导模型输出有害内容。
3. 实验或效果：在开源和闭源模型上实现较高攻击成功率，优于现有越狱攻击方法。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) are widely used in various fields due to their powerful cross-modal comprehension and generation capabilities. However, more modalities bring more vulnerabilities to being utilized for jailbreak attacks, which induces MLLMs to output harmful content. Due to the strong reasoning ability of MLLMs, previous jailbreak attacks try to explore reasoning safety risk in text modal, while similar threats have been largely overlooked in the visual modal. To fully evaluate potential safety risks in the visual reasoning task, we propose Visual Reasoning Sequential Attack (VRSA), which induces MLLMs to gradually externalize and aggregate complete harmful intent by decomposing the original harmful text into several sequentially related sub-images. In particular, to enhance the rationality of the scene in the image sequence, we propose Adaptive Scene Refinement to optimize the scene most relevant to the original harmful query. To ensure the semantic continuity of the generated image, we propose Semantic Coherent Completion to iteratively rewrite each sub-text combined with contextual information in this scene. In addition, we propose Text-Image Consistency Alignment to keep the semantical consistency. A series of experiments demonstrates that the VRSA can achieve a higher attack success rate compared with the state-of-the-art jailbreak attack methods on both the open-source and closed-source MLLMs such as GPT-4o and Claude-4.5-Sonnet.

