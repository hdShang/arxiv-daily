---
layout: default
title: Security Risk of Misalignment between Text and Image in Multi-modal Model
---

# Security Risk of Misalignment between Text and Image in Multi-modal Model

**arXiv**: [2510.26105v1](https://arxiv.org/abs/2510.26105) | [PDF](https://arxiv.org/pdf/2510.26105.pdf)

**作者**: Xiaosen Wang, Zhijin Ge, Shaokang Wang

---

## 💡 一句话要点

**提出PReMA攻击方法，通过修改图像操纵多模态扩散模型输出，应对固定提示场景的安全风险。**

**关键词**: `多模态扩散模型` `对抗攻击` `文本图像对齐` `NSFW内容生成` `图像编辑安全` `PReMA攻击`

## 📋 核心要点

1. 核心问题：多模态扩散模型中文本与图像对齐不足，易生成不当内容，如NSFW。
2. 方法要点：PReMA仅创建对抗图像，无需修改提示，即可操纵模型生成内容。
3. 实验或效果：在图像修复和风格迁移任务中验证PReMA有效性，威胁模型完整性。

## 📄 摘要（原文）

> Despite the notable advancements and versatility of multi-modal diffusion
> models, such as text-to-image models, their susceptibility to adversarial
> inputs remains underexplored. Contrary to expectations, our investigations
> reveal that the alignment between textual and Image modalities in existing
> diffusion models is inadequate. This misalignment presents significant risks,
> especially in the generation of inappropriate or Not-Safe-For-Work (NSFW)
> content. To this end, we propose a novel attack called Prompt-Restricted
> Multi-modal Attack (PReMA) to manipulate the generated content by modifying the
> input image in conjunction with any specified prompt, without altering the
> prompt itself. PReMA is the first attack that manipulates model outputs by
> solely creating adversarial images, distinguishing itself from prior methods
> that primarily generate adversarial prompts to produce NSFW content.
> Consequently, PReMA poses a novel threat to the integrity of multi-modal
> diffusion models, particularly in image-editing applications that operate with
> fixed prompts. Comprehensive evaluations conducted on image inpainting and
> style transfer tasks across various models confirm the potent efficacy of
> PReMA.

