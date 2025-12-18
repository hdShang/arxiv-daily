---
layout: default
title: FlexAC: Towards Flexible Control of Associative Reasoning in Multimodal Large Language Models
---

# FlexAC: Towards Flexible Control of Associative Reasoning in Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11190" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11190v3</a>
  <a href="https://arxiv.org/pdf/2510.11190.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11190v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.11190v3', 'FlexAC: Towards Flexible Control of Associative Reasoning in Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengming Yuan, Xinyu Lyu, Shuailong Wang, Beitao Chen, Jingkuan Song, Lianli Gao

**分类**: cs.CV

**发布日期**: 2025-10-13 (更新: 2025-11-06)

**备注**: 19 pages, 11 figures. Accepted by the 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

**🔗 代码/项目**: [GITHUB](https://github.com/ylhz/FlexAC)

---

## 💡 一句话要点

**FlexAC：面向多模态大语言模型中联想推理的灵活控制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `联想推理` `灵活控制` `幻觉引导` `steering vectors`

## 📋 核心要点

1. 现有MLLM方法在忠实性和创造性之间难以平衡，缺乏对联想推理强度的灵活控制。
2. FlexAC通过幻觉引导和steering vectors，在中间层调节模型表示，实现联想推理强度的灵活控制。
3. 实验表明，FlexAC在创造力方面提升显著，并有效降低了幻觉率，优于现有基线。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)面临着忠实性和创造性之间的内在权衡，因为不同的任务需要不同程度的联想推理。然而，现有方法缺乏调节这种推理强度的灵活性，限制了MLLMs在事实性和创造性场景中的适应性。为了弥合这一差距，我们提出为MLLMs配备能够灵活控制联想推理的机制。我们首先研究了MLLMs中联想行为的内部机制，发现：(1)中间层在塑造模型的联想倾向方面起着关键作用，(2)修改这些层中的表示可以有效地调节联想推理强度，(3)可以利用幻觉来导出指导这种调节的steering vectors。在此基础上，我们引入了Flexible Association Control (FlexAC)，这是一个轻量级的、免训练的框架，用于调节MLLMs中的联想行为。FlexAC首先诱导幻觉引导的中间表示来编码联想方向。然后，它选择高联想实例来构建有效的联想steering vectors，其强度经过自适应校准，以平衡创造性指导和输出稳定性。最后，认识到联想推理的多维性质，FlexAC结合了从少量目标领域样本的前向传递中导出的特定于任务的联想向量，使模型能够遵循不同的联想方向，更好地适应创造性任务。值得注意的是，我们的方法在Creation-MMBench上实现了高达5.8倍的创造力提升，在CHAIR上实现了29%的幻觉率降低，超过了现有的基线，证明了其在实现MLLMs中联想推理的灵活控制方面的有效性。

## 🔬 方法详解

**问题定义**：多模态大语言模型(MLLMs)在处理不同任务时，需要在忠实性和创造性之间进行权衡。现有方法缺乏对联想推理强度的灵活控制，导致模型难以适应不同的场景需求，例如在需要事实准确性的任务中可能过于发散，而在需要创造性的任务中又可能过于保守。

**核心思路**：FlexAC的核心思路是通过调节模型中间层的表示来控制联想推理的强度。该方法利用幻觉来引导模型产生联想方向，并构建steering vectors来调整中间层的表示，从而实现对联想推理的灵活控制。通过这种方式，模型可以根据任务需求，自适应地调整联想推理的强度，从而在忠实性和创造性之间取得平衡。

**技术框架**：FlexAC框架主要包含以下几个阶段：1) **幻觉引导的中间表示编码**：利用幻觉来引导模型产生联想方向，并将这些方向编码到中间层的表示中。2) **联想steering vectors构建**：选择高联想实例来构建有效的联想steering vectors，这些向量用于调整中间层的表示。3) **steering vectors强度自适应校准**：自适应地校准steering vectors的强度，以平衡创造性指导和输出稳定性。4) **任务特定联想向量融合**：结合从少量目标领域样本中导出的任务特定联想向量，使模型能够更好地适应创造性任务。

**关键创新**：FlexAC的关键创新在于：1) **利用幻觉引导联想方向**：通过诱导模型产生幻觉，来探索潜在的联想方向，从而为联想推理提供更丰富的指导。2) **中间层表示调节**：通过调整模型中间层的表示，来实现对联想推理强度的直接控制，避免了对整个模型的微调。3) **steering vectors强度自适应校准**：根据任务需求，自适应地调整steering vectors的强度，从而在创造性和稳定性之间取得平衡。

**关键设计**：FlexAC的关键设计包括：1) **中间层选择**：选择对联想推理影响最大的中间层进行调节。2) **幻觉诱导方法**：采用特定的方法来诱导模型产生有意义的幻觉。3) **steering vectors构建方法**：选择高联想实例来构建有效的steering vectors。4) **强度校准策略**：设计自适应的强度校准策略，以平衡创造性和稳定性。具体的参数设置和网络结构细节在论文中进行了详细描述，例如如何选择中间层，如何生成幻觉，以及如何计算和应用steering vectors。

## 📊 实验亮点

FlexAC在Creation-MMBench上实现了高达5.8倍的创造力提升，并在CHAIR上实现了29%的幻觉率降低，显著优于现有基线方法。这些实验结果表明，FlexAC能够有效地控制MLLMs中的联想推理，并在创造性和忠实性之间取得更好的平衡。该方法无需训练，易于部署和应用。

## 🎯 应用场景

FlexAC可应用于各种需要平衡忠实性和创造性的多模态任务，例如图像描述生成、故事创作、创意广告设计等。该方法能够提升模型在创意生成任务中的表现，并降低在事实性任务中的幻觉率，具有广泛的应用前景和实际价值。未来，可以进一步探索FlexAC在其他多模态任务中的应用，并研究如何将其与其他技术相结合，以提升模型的整体性能。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) face an inherent trade-off between faithfulness and creativity, as different tasks require varying degrees of associative reasoning. However, existing methods lack the flexibility to modulate this reasoning strength, limiting MLLMs' adaptability across factual and creative scenarios. To bridge this gap, we propose equipping MLLMs with mechanisms that enable flexible control over associative reasoning. We begin by investigating the internal mechanisms underlying associative behavior in MLLMs and find that: (1) middle layers play a pivotal role in shaping model's associative tendencies, (2) modifying representations in these layers effectively regulates associative reasoning strength, and (3) hallucinations can be exploited to derive steering vectors that guide this modulation. Building on these findings, we introduce Flexible Association Control (FlexAC), a lightweight and training-free framework for modulating associative behavior in MLLMs. FlexAC first induces hallucination-guided intermediate representations to encode associative directions. Then, it selects high-association instances to construct effective associative steering vectors, whose strengths are adaptively calibrated to balance creative guidance with output stability. Finally, recognizing the multi-dimensional nature of associative reasoning, FlexAC incorporates task-specific associative vectors derived from a forward pass on a few target-domain samples, enabling models to follow diverse associative directions and better adapt to creative tasks. Notably, our method achieves up to a 5.8x improvement in creativity on Creation-MMBench and a 29% reduction in hallucination rate on CHAIR, surpassing existing baselines and demonstrating its effectiveness in enabling flexible control over associative reasoning in MLLMs. Our code is available at https://github.com/ylhz/FlexAC.

