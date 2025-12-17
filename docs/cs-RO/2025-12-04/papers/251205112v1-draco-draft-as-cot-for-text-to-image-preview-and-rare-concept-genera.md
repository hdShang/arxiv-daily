---
layout: default
title: DraCo: Draft as CoT for Text-to-Image Preview and Rare Concept Generation
---

# DraCo: Draft as CoT for Text-to-Image Preview and Rare Concept Generation

**arXiv**: [2512.05112v1](https://arxiv.org/abs/2512.05112) | [PDF](https://arxiv.org/pdf/2512.05112.pdf)

**作者**: Dongzhi Jiang, Renrui Zhang, Haodong Li, Zhuofan Zong, Ziyu Guo, Jun He, Claire Guo, Junyan Ye, Rongyao Fang, Weijia Li, Rui Liu, Hongsheng Li

---

## 💡 一句话要点

**提出DraCo方法，通过草稿图像作为思维链，提升文本到图像生成的预览与罕见概念生成能力。**

**关键词**: `文本到图像生成` `思维链推理` `草稿图像预览` `罕见概念生成` `选择性修正` `多模态大语言模型`

## 📋 核心要点

1. 现有方法依赖抽象文本规划，导致文本到图像生成中规划粒度粗和罕见属性组合生成困难。
2. DraCo首先生成低分辨率草稿图像作为视觉规划，然后利用模型理解能力验证语义对齐并进行选择性修正。
3. 在GenEval等基准上，DraCo相比直接生成和其他CoT方法取得显著性能提升，如GenEval增加8%。

## 📄 摘要（原文）

> Recent unified multimodal large language models (MLLMs) have shown impressive capabilities, incorporating chain-of-thought (CoT) reasoning for enhanced text-to-image generation. However, existing approaches remain limited, either treating the model merely as a standalone generator or relying on abstract textual planning. To this end, we propose Draft-as-CoT (DraCo), a novel interleaved reasoning paradigm that fully leverages both textual and visual contents in CoT for better planning and verification. Our method first generates a low-resolution draft image as preview, providing more concrete and structural visual planning and guidance. Then, we employ the model's inherent understanding capability to verify potential semantic misalignments between the draft and input prompt, and performs refinement through selective corrections with super-resolution. In this way, our approach addresses two fundamental challenges: the coarse-grained nature of textual planning and the difficulty in generating rare attribute combinations. To support training, we curate DraCo-240K, aiming to enhance three atomic capabilities spanning general correction, instance manipulation, and layout reorganization. Supported by DraCo-CFG, a specialized classifier-free guidance (CFG) strategy for interleaved reasoning, DraCo achieves a tremendous increase on GenEval (+8%), Imagine-Bench (+0.91), and GenEval++ (+3%), significantly outperforming direct generation and other generation methods empowered by CoT.

