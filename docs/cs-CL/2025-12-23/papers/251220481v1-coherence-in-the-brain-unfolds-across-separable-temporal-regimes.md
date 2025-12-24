---
layout: default
title: Coherence in the brain unfolds across separable temporal regimes
---

# Coherence in the brain unfolds across separable temporal regimes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20481" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20481v1</a>
  <a href="https://arxiv.org/pdf/2512.20481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20481v1', 'Coherence in the brain unfolds across separable temporal regimes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davide Stauba, Finn Rabe, Akhil Misra, Yves Pauli, Roya Hüppi, Nils Lang, Lars Michels, Victoria Edkins, Sascha Frühholz, Iris Sommer, Wolfram Hinzen, Philipp Homan

**分类**: q-bio.NC, cs.CL

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**利用LLM提取的漂移和位移信号，揭示大脑中语言连贯性处理的时域分离机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言理解` `大脑连贯性` `大型语言模型` `fMRI` `默认模式网络` `事件驱动` `神经机制`

## 📋 核心要点

1. 自然语言理解中，大脑需要在长时程的语义积累和短时程的事件边界快速重构之间进行平衡，现有研究缺乏对这两种机制如何在大脑中实现的清晰理解。
2. 本文利用大型语言模型（LLM）提取的漂移和位移信号，分别对应语境的逐渐变化和事件的突变，以此来捕捉大脑中的语义积累和快速重构过程。
3. 实验结果表明，漂移信号主要与默认模式网络相关，而位移信号主要与听觉皮层和语言联合皮层相关，揭示了大脑中语言连贯性处理的时域分离机制。

## 📝 摘要（中文）

语言连贯性要求大脑满足两个相互竞争的时间需求：跨越扩展语境的意义逐渐积累，以及在事件边界处的表征快速重构。尽管这些过程对于语言和思维至关重要，但它们在人类大脑中自然听觉过程中的实现方式仍不清楚。本文测试了这两个过程是否可以通过无标注的漂移和位移信号来捕捉，以及它们的大脑神经表达是否在大规模皮层系统中分离。这些信号来自大型语言模型（LLM），并直接从叙事输入中形式化了语境漂移和事件位移。为了实现具有稳定参数估计的高精度体素编码模型，我们对一位健康成年人进行了超过7小时的密集采样，同时收集了超高场（7T）BOLD数据。然后，我们使用在独立故事上验证的正则化编码框架，对特征信息引导的血流动力学反应进行建模。漂移预测主要出现在默认模式网络中心，而位移预测在初级听觉皮层和语言联合皮层双侧均很明显。此外，默认模式网络和顶叶网络中的活动最好由一个信号来解释，该信号捕捉了意义如何在叙事过程中积累和逐渐消退。总之，这些发现表明，语言理解过程中的连贯性是通过缓慢的语境整合和快速的事件驱动重构的可分离神经机制来实现的，为理解精神疾病中语言连贯性障碍提供了一个机械论的切入点。

## 🔬 方法详解

**问题定义**：论文旨在解决自然语言理解过程中，大脑如何同时处理长时程的语义连贯性（语境积累）和短时程的事件边界（快速重构）的问题。现有方法难以区分这两种时间尺度上的神经活动，并且缺乏对它们之间相互作用的深入理解。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）来提取两种关键信号：语境漂移信号（contextual drift）和事件位移信号（event shift）。语境漂移信号反映了随着叙事展开，语义逐渐积累和变化的过程；事件位移信号则捕捉了叙事中事件边界处的突变。通过将这些信号与大脑活动进行关联，可以揭示大脑中不同区域在不同时间尺度上处理语言连贯性的方式。

**技术框架**：整体框架包括以下几个主要步骤：
1. **数据采集**：使用7T超高场fMRI扫描，记录被试在听取多个犯罪故事时的脑活动。
2. **LLM特征提取**：使用大型语言模型处理故事文本，提取语境漂移和事件位移信号。
3. **编码模型构建**：使用正则化的编码框架，将LLM提取的信号与fMRI数据进行关联，构建体素级别的预测模型。
4. **模型验证**：在独立的故事上验证模型的预测能力，评估模型的泛化性能。
5. **结果分析**：分析不同脑区对语境漂移和事件位移信号的响应，揭示大脑中语言连贯性处理的时域分离机制。

**关键创新**：论文的关键创新在于：
1. **使用LLM提取的漂移和位移信号**：这种方法能够更准确地捕捉语言理解过程中的语义变化和事件边界，避免了传统方法中手动标注的局限性。
2. **高精度体素编码模型**：通过高密度采样和正则化方法，构建了具有稳定参数估计的体素编码模型，提高了模型预测的准确性。
3. **揭示了大脑中语言连贯性处理的时域分离机制**：研究结果表明，大脑中存在两个不同的神经机制，分别负责处理长时程的语义积累和短时程的事件重构。

**关键设计**：
* **LLM选择**：论文使用了具体哪个LLM未明确说明（未知）。
* **正则化方法**：使用了正则化编码框架，具体正则化方法未知。
* **7T fMRI**：使用7T超高场fMRI，提供更高分辨率的脑活动数据。
* **编码模型**：体素级别的编码模型，将LLM特征与每个体素的BOLD信号关联。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20481v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20481v1/figure2_meanr_simesp.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20481v1/figure3_contrasts.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

研究发现，默认模式网络（DMN）的活动与语境漂移信号显著相关，表明DMN在长时程的语义整合中起着关键作用。而初级听觉皮层和语言联合皮层则对事件位移信号更加敏感，反映了这些区域在快速事件重构中的作用。此外，研究还发现顶叶网络也参与了语义积累和消退的过程，进一步揭示了语言理解的复杂神经机制。

## 🎯 应用场景

该研究成果可应用于精神疾病的诊断和治疗，例如精神分裂症患者常常表现出语言连贯性障碍。通过分析患者大脑中漂移和位移信号的异常，可以帮助医生更准确地诊断病情，并制定更有效的治疗方案。此外，该研究还可以用于开发更智能的自然语言处理系统，提高机器对人类语言的理解能力。

## 📄 摘要（原文）

> Coherence in language requires the brain to satisfy two competing temporal demands: gradual accumulation of meaning across extended context and rapid reconfiguration of representations at event boundaries. Despite their centrality to language and thought, how these processes are implemented in the human brain during naturalistic listening remains unclear. Here, we tested whether these two processes can be captured by annotation-free drift and shift signals and whether their neural expression dissociates across large-scale cortical systems. These signals were derived from a large language model (LLM) and formalized contextual drift and event shifts directly from the narrative input. To enable high-precision voxelwise encoding models with stable parameter estimates, we densely sampled one healthy adult across more than 7 hours of listening to thirteen crime stories while collecting ultra high-field (7T) BOLD data. We then modeled the feature-informed hemodynamic response using a regularized encoding framework validated on independent stories. Drift predictions were prevalent in default-mode network hubs, whereas shift predictions were evident bilaterally in the primary auditory cortex and language association cortex. Furthermore, activity in default-mode and parietal networks was best explained by a signal capturing how meaning accumulates and gradually fades over the course of the narrative. Together, these findings show that coherence during language comprehension is implemented through dissociable neural regimes of slow contextual integration and rapid event-driven reconfiguration, offering a mechanistic entry point for understanding disturbances of language coherence in psychiatric disorders.

