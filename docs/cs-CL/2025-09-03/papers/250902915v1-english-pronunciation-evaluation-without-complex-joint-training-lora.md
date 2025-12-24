---
layout: default
title: "English Pronunciation Evaluation without Complex Joint Training: LoRA Fine-tuned Speech Multimodal LLM"
---

# English Pronunciation Evaluation without Complex Joint Training: LoRA Fine-tuned Speech Multimodal LLM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02915" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02915v1</a>
  <a href="https://arxiv.org/pdf/2509.02915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02915v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02915v1', 'English Pronunciation Evaluation without Complex Joint Training: LoRA Fine-tuned Speech Multimodal LLM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taekyung Ahn, Hosung Nam

**分类**: cs.CL

**发布日期**: 2025-09-03

---

## 💡 一句话要点

**利用LoRA微调多模态LLM实现高效英语发音评估与诊断**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `低秩适应` `发音评估` `语音识别` `大型语言模型` `迁移学习` `计算机辅助语言学习`

## 📋 核心要点

1. 现有发音评估方法通常需要复杂的架构设计和针对不同任务的独立训练流程，效率较低。
2. 本研究提出利用LoRA微调多模态LLM，无需复杂架构修改即可同时实现APA和MDD。
3. 实验结果表明，该方法在发音评估任务上取得了与人工评估高度相关的性能，且错误率较低。

## 📝 摘要（中文）

本研究表明，通过低秩适应(LoRA)调整的多模态大型语言模型(MLLM)能够同时执行自动发音评估(APA)和发音错误检测与诊断(MDD)。该方法利用微软的Phi-4-multimodal-instruct模型，无需复杂的架构更改或传统上用于这些不同任务的独立训练程序。在Speechocean762数据集上进行微调后，模型预测的发音评估分数与人工分配的分数表现出很强的皮尔逊相关系数(PCC > 0.7)，同时实现了较低的词错误率(WER)和音素错误率(PER)(均 < 0.15)。值得注意的是，仅微调LoRA层就足以达到与微调所有音频层相当的性能水平。这项研究强调，通过调整大型多模态模型，无需完全微调，就可以建立一个集成的发音评估系统，与以前为同时进行APA和MDD而设计的联合模型相比，该方法采用了一种显著更简单的训练方法。这种高效的基于LoRA的方法为英语L2学习者提供了更易于访问、集成和有效的计算机辅助发音训练(CAPT)技术。

## 🔬 方法详解

**问题定义**：论文旨在解决英语发音评估与诊断问题，具体包括自动发音评估(APA)和发音错误检测与诊断(MDD)。现有方法通常需要针对APA和MDD分别设计复杂的模型架构和训练流程，或者采用联合训练的方式，但计算成本高昂且不易部署。因此，如何高效地构建一个集成的发音评估系统是本研究要解决的核心问题。

**核心思路**：论文的核心思路是利用预训练的多模态大型语言模型(MLLM)的强大表征能力，通过低秩适应(LoRA)技术进行微调，使其能够同时执行APA和MDD任务。LoRA通过引入少量可训练参数来调整预训练模型的权重，从而避免了对整个模型进行微调，大大降低了计算成本和存储需求。

**技术框架**：整体框架基于微软的Phi-4-multimodal-instruct模型，该模型是一个预训练的多模态LLM。研究人员首先将语音数据输入模型，然后利用LoRA技术对模型的特定层进行微调。微调后的模型可以同时输出APA分数和MDD结果。整个流程包括数据预处理、模型微调和结果评估三个主要阶段。

**关键创新**：最重要的技术创新点在于利用LoRA技术对多模态LLM进行微调，从而实现高效的集成发音评估系统。与现有方法相比，该方法无需复杂的架构设计和独立的训练流程，大大简化了训练过程，降低了计算成本。此外，该方法仅微调LoRA层即可达到与微调所有音频层相当的性能水平，进一步提高了效率。

**关键设计**：论文使用Speechocean762数据集进行微调，该数据集包含大量的英语发音数据和人工标注。在LoRA微调过程中，研究人员选择了模型的特定层进行调整，并设置了合适的学习率和训练轮数。损失函数的设计需要同时考虑APA和MDD任务的需求，可能采用了加权损失函数或者多任务学习的方法。具体的网络结构细节和参数设置在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

实验结果表明，通过LoRA微调的多模态LLM在Speechocean762数据集上取得了显著的性能提升。模型预测的发音评估分数与人工分配的分数表现出很强的皮尔逊相关系数(PCC > 0.7)，同时实现了较低的词错误率(WER)和音素错误率(PER)(均 < 0.15)。值得注意的是，仅微调LoRA层就足以达到与微调所有音频层相当的性能水平，验证了该方法的效率和有效性。

## 🎯 应用场景

该研究成果可应用于计算机辅助发音训练(CAPT)系统，帮助英语L2学习者提高发音水平。该方法能够提供自动发音评估和错误诊断，为学习者提供个性化的反馈和指导。此外，该技术还可以应用于语音识别、语音合成等领域，提高语音处理系统的性能和鲁棒性。未来，该研究有望推动更智能、更高效的语言学习工具的发展。

## 📄 摘要（原文）

> This study demonstrates that a Multimodal Large Language Model (MLLM) adapted via Low-Rank Adaptation (LoRA) can perform both Automatic Pronunciation Assessment (APA) and Mispronunciation Detection and Diagnosis (MDD) simultaneously. Leveraging Microsoft's Phi-4-multimodal-instruct, our fine-tuning method eliminates the need for complex architectural changes or separate training procedures conventionally required for these distinct tasks. Fine-tuned on the Speechocean762 dataset, the pronunciation evaluation scores predicted by the model exhibited a strong Pearson Correlation Coefficient (PCC > 0.7) with human-assigned scores, while achieving low Word Error Rate (WER) and Phoneme Error Rate (PER) (both < 0.15). Notably, fine-tuning only the LoRA layers was sufficient to achieve performance levels comparable to those achieved by fine-tuning all audio layers. This research highlights that an integrated pronunciation assessment system can be established by adapting large multimodal models without full fine-tuning, utilizing a significantly simpler training methodology compared to previous joint models designed for simultaneous APA and MDD. This efficient LoRA-based approach paves the way for more accessible, integrated, and effective Computer-Assisted Pronunciation Training (CAPT) technologies for English L2 learners.

