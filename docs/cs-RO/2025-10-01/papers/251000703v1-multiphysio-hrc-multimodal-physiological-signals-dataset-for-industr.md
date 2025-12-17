---
layout: default
title: MultiPhysio-HRC: Multimodal Physiological Signals Dataset for industrial Human-Robot Collaboration
---

# MultiPhysio-HRC: Multimodal Physiological Signals Dataset for industrial Human-Robot Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00703" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00703v1</a>
  <a href="https://arxiv.org/pdf/2510.00703.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00703v1" onclick="toggleFavorite(this, '2510.00703v1', 'MultiPhysio-HRC: Multimodal Physiological Signals Dataset for industrial Human-Robot Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrea Bussolan, Stefano Baraldo, Oliver Avram, Pablo Urcola, Luis Montesano, Luca Maria Gambardella, Anna Valente

**分类**: cs.RO

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**MultiPhysio-HRC：用于工业人机协作的多模态生理信号数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机协作` `多模态数据集` `生理信号` `情感计算` `认知负荷` `工业机器人` `心理生理状态` `虚拟现实`

## 📋 核心要点

1. 现有的人机协作系统缺乏对人类心理生理状态的感知，难以实现自适应和以人为本的交互。
2. MultiPhysio-HRC数据集通过整合生理、音频和面部数据，全面捕捉人类在人机协作中的精神状态。
3. 基线模型在压力和认知负荷分类上的评估结果，验证了数据集在情感计算和人机协作研究中的价值。

## 📝 摘要（中文）

本文介绍了MultiPhysio-HRC，一个多模态数据集，包含在真实人机协作（HRC）场景中收集的生理、音频和面部数据。该数据集包括脑电图（EEG）、心电图（ECG）、皮肤电活动（EDA）、呼吸（RESP）、肌电图（EMG）、语音记录和面部动作单元。数据集整合了受控认知任务、沉浸式虚拟现实体验以及手动和机器人辅助的工业拆卸活动，以全面捕捉参与者的精神状态。通过验证的心理自评问卷获得了丰富的ground truth标注。对压力和认知负荷分类的基线模型进行了评估，证明了该数据集在情感计算和以人为本的机器人研究中的潜力。MultiPhysio-HRC是公开可用的，旨在支持以人为中心的自动化、工作场所福祉和智能机器人系统方面的研究。

## 🔬 方法详解

**问题定义**：现有的人机协作系统难以准确感知人类操作者的心理生理状态，如压力和认知负荷，这限制了机器人根据人类状态进行自适应调整的能力。缺乏高质量、多模态的数据集是开发此类系统的主要瓶颈。现有数据集可能缺乏真实工业场景的数据，或者模态单一，难以全面反映人类状态。

**核心思路**：MultiPhysio-HRC数据集的核心思路是通过在真实的工业人机协作场景中，同步采集多种生理信号、音频和面部数据，并结合心理自评问卷，构建一个全面、高质量的多模态数据集。该数据集旨在为开发能够感知人类状态并进行自适应调整的智能机器人系统提供数据支持。

**技术框架**：MultiPhysio-HRC数据集的构建流程包括以下几个主要阶段：
1. **实验设计**：设计包含受控认知任务、虚拟现实体验和工业拆卸活动（手动和机器人辅助）的实验场景。
2. **数据采集**：同步采集参与者的脑电图（EEG）、心电图（ECG）、皮肤电活动（EDA）、呼吸（RESP）、肌电图（EMG）、语音记录和面部动作单元等数据。
3. **数据标注**：使用验证的心理自评问卷获取参与者的主观心理状态评估，作为ground truth。
4. **数据预处理**：对采集到的数据进行清洗、校准和同步处理。
5. **数据集发布**：将处理后的数据集公开，供研究人员使用。

**关键创新**：MultiPhysio-HRC数据集的关键创新在于：
1. **多模态融合**：同时采集多种生理信号、音频和面部数据，提供更全面的信息。
2. **真实场景**：数据采集于真实的工业人机协作场景，更具实用价值。
3. **丰富标注**：结合心理自评问卷，提供高质量的ground truth标注。

**关键设计**：数据集包含多种类型的任务，包括：
*   **受控认知任务**：用于诱发特定的认知状态。
*   **虚拟现实体验**：提供沉浸式的交互环境。
*   **工业拆卸活动**：模拟真实的人机协作场景。

生理信号的采样率根据不同模态进行调整，以保证数据质量。心理自评问卷采用标准化的量表，以保证评估的可靠性。

## 📊 实验亮点

论文通过基线模型在压力和认知负荷分类任务上的评估，验证了MultiPhysio-HRC数据集的有效性。实验结果表明，基于该数据集训练的模型能够较好地识别参与者的心理生理状态。虽然具体的性能数据未在摘要中给出，但该结果证明了数据集在情感计算和人机协作研究中的潜力，为后续研究奠定了基础。

## 🎯 应用场景

MultiPhysio-HRC数据集可广泛应用于人机协作、情感计算、工作场所福祉和智能机器人系统等领域。通过该数据集，研究人员可以开发能够感知人类心理生理状态并进行自适应调整的机器人系统，从而提高工作效率，改善工作环境，并提升人类的福祉。未来，该数据集可以扩展到更多工业场景和任务，为更智能、更人性化的人机协作系统提供数据支持。

## 📄 摘要（原文）

> Human-robot collaboration (HRC) is a key focus of Industry 5.0, aiming to enhance worker productivity while ensuring well-being. The ability to perceive human psycho-physical states, such as stress and cognitive load, is crucial for adaptive and human-aware robotics. This paper introduces MultiPhysio-HRC, a multimodal dataset containing physiological, audio, and facial data collected during real-world HRC scenarios. The dataset includes electroencephalography (EEG), electrocardiography (ECG), electrodermal activity (EDA), respiration (RESP), electromyography (EMG), voice recordings, and facial action units. The dataset integrates controlled cognitive tasks, immersive virtual reality experiences, and industrial disassembly activities performed manually and with robotic assistance, to capture a holistic view of the participants' mental states. Rich ground truth annotations were obtained using validated psychological self-assessment questionnaires. Baseline models were evaluated for stress and cognitive load classification, demonstrating the dataset's potential for affective computing and human-aware robotics research. MultiPhysio-HRC is publicly available to support research in human-centered automation, workplace well-being, and intelligent robotic systems.

