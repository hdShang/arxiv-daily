---
layout: default
title: MaskCD: Mitigating LVLM Hallucinations by Image Head Masked Contrastive Decoding
---

# MaskCD: Mitigating LVLM Hallucinations by Image Head Masked Contrastive Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02790" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02790v1</a>
  <a href="https://arxiv.org/pdf/2510.02790.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02790v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02790v1', 'MaskCD: Mitigating LVLM Hallucinations by Image Head Masked Contrastive Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyuan Deng, Yujiu Yang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-10-03

**备注**: accepted to emnlp2025 findings

**🔗 代码/项目**: [GITHUB](https://github.com/Deng-Jingyuan/MaskCD)

---

## 💡 一句话要点

**提出MaskCD，通过图像头掩码对比解码缓解LVLM幻觉问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型视觉语言模型` `幻觉缓解` `对比解码` `图像头掩码` `多模态学习`

## 📋 核心要点

1. 现有LVLM容易产生幻觉，即生成与输入视觉和文本内容矛盾的信息，现有对比解码方法难以构建合适的对比样本，注意力操纵方法则缺乏稳定性。
2. MaskCD的核心思想是利用LVLM中的“图像头”，通过掩码图像头来构建对比样本，用于对比解码，从而抑制幻觉。
3. 在LLaVA-1.5-7b和Qwen-VL-7b上，MaskCD在CHAIR、POPE、AMBER和MME等基准测试中有效缓解了幻觉现象，并保持了LVLM的通用能力。

## 📝 摘要（中文）

大型视觉语言模型(LVLMs)在下游多模态任务的视觉语言理解方面表现出卓越的性能。然而，随着能力的提升，问题也随之出现。其中，幻觉问题备受关注，指的是LVLMs生成与其输入视觉和文本内容相矛盾的内容的现象。许多方法被提出以解决这个问题，例如对比解码和注意力操纵。然而，对比解码方法在构建合适的对比样本方面存在困难，而注意力操纵方法高度敏感，缺乏稳定性。在这项工作中，我们提出了图像头掩码对比解码(MaskCD)。我们的方法利用LVLMs中的“图像头”，通过掩盖它们来构建对比解码的对比样本。我们使用CHAIR、POPE、AMBER和MME等各种基准在LLaVA-1.5-7b和Qwen-VL-7b上评估了MaskCD。结果表明，MaskCD有效地缓解了幻觉现象，并保留了LVLMs的通用能力。相应的资源可以在https://github.com/Deng-Jingyuan/MaskCD 找到。

## 🔬 方法详解

**问题定义**：论文旨在解决大型视觉语言模型（LVLM）中存在的幻觉问题，即模型生成与输入图像和文本内容相矛盾的信息。现有的对比解码方法难以构建有效的对比样本，而注意力机制调整方法又过于敏感，缺乏稳定性，导致幻觉问题难以有效缓解。

**核心思路**：MaskCD的核心思路是利用LVLM中负责处理图像信息的“图像头”，通过对这些图像头进行掩码操作，生成与原始图像信息略有差异的对比样本。然后，利用这些对比样本进行对比解码，鼓励模型生成与原始图像信息一致的文本描述，从而抑制幻觉。这种方法避免了手动设计对比样本的困难，并降低了对注意力机制的过度依赖。

**技术框架**：MaskCD的技术框架主要包含以下几个步骤：1) 输入图像和文本提示；2) 通过LVLM的图像编码器提取图像特征；3) 对图像编码器的“图像头”进行掩码操作，生成对比图像特征；4) 将原始图像特征和对比图像特征分别输入到LVLM的文本解码器中；5) 利用对比解码损失函数，鼓励模型生成与原始图像特征一致的文本描述，抑制与对比图像特征相关的幻觉信息。

**关键创新**：MaskCD的关键创新在于利用“图像头掩码”来自动生成对比样本。与手动构建或使用对抗攻击生成对比样本的方法相比，这种方法更加高效且易于实现。此外，MaskCD直接作用于LVLM的内部结构，能够更好地利用模型自身的知识来抑制幻觉。

**关键设计**：MaskCD的关键设计包括：1) 图像头掩码策略：如何选择需要掩码的图像头，以及掩码的比例；2) 对比解码损失函数：如何设计损失函数来有效地鼓励模型生成与原始图像信息一致的文本描述；3) 超参数设置：例如，对比解码的温度系数等。

## 📊 实验亮点

MaskCD 在 LLaVA-1.5-7b 和 Qwen-VL-7b 模型上进行了评估，并在 CHAIR、POPE、AMBER 和 MME 等多个基准测试中取得了显著的性能提升。实验结果表明，MaskCD 能够有效缓解 LVLM 的幻觉问题，同时保持了模型原有的通用能力。具体提升幅度在不同数据集和模型上有所不同，但总体趋势是正向的。

## 🎯 应用场景

MaskCD 有潜力应用于各种需要可靠视觉语言理解的场景，例如：医疗影像诊断，自动驾驶，智能客服，以及视觉辅助工具等。通过减少LVLM的幻觉，可以提高这些应用的可信度和安全性，并最终提升用户体验。未来，该技术可以进一步扩展到其他多模态任务，例如视频理解和语音识别。

## 📄 摘要（原文）

> Large vision-language models (LVLMs) have shown remarkable performance in visual-language understanding for downstream multimodal tasks. While their capabilities are improving, problems emerge simultaneously. Among those problems, the hallucinations have attracted much attention, which stands for the phenomenon where LVLMs generate contradictory content to their input visual and text contents. Many approaches have been proposed to deal with this issue, such as contrastive decoding and attention manipulation. However, contrastive decoding methods struggle in constructing appropriate contrastive samples, and attention manipulation methods are highly sensitive, lacking stability. In this work, we propose image head Masked Contrastive Decoding (MaskCD). Our approach utilizes the "image heads" in LVLMs, masking them to construct contrastive samples for contrastive decoding. We evaluated MaskCD on LLaVA-1.5-7b and Qwen-VL-7b, using various benchmarks such as CHAIR, POPE, AMBER and MME. The results demonstrate that MaskCD effectively alleviates the phenomenon of hallucinations and retains the general capabilities of LVLMs. Corresponding resources could be found at: https://github.com/Deng-Jingyuan/MaskCD .

