---
layout: default
title: "ShizhenGPT: Towards Multimodal LLMs for Traditional Chinese Medicine"
---

# ShizhenGPT: Towards Multimodal LLMs for Traditional Chinese Medicine

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14706" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14706v1</a>
  <a href="https://arxiv.org/pdf/2508.14706.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14706v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14706v1', 'ShizhenGPT: Towards Multimodal LLMs for Traditional Chinese Medicine')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junying Chen, Zhenyang Cai, Zhiheng Liu, Yunjin Yang, Rongsheng Wang, Qingying Xiao, Xiangyi Feng, Zhan Su, Jing Guo, Xiang Wan, Guangjun Yu, Haizhou Li, Benyou Wang

**分类**: cs.CL, cs.AI, cs.CV, cs.LG, cs.MM

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出ShizhenGPT以解决中医领域多模态数据稀缺问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `传统中医学` `大型语言模型` `数据集构建` `视觉理解` `医学诊断` `深度学习`

## 📋 核心要点

1. 现有大型语言模型在传统中医领域的应用受到数据稀缺和多模态特性限制，难以有效进行中医诊断。
2. 论文提出ShizhenGPT，结合了大规模中医数据集和多模态学习，旨在提升中医知识的理解和推理能力。
3. 实验结果显示，ShizhenGPT在中医资格考试和视觉诊断基准测试中表现优于同规模模型，并与更大模型竞争。

## 📝 摘要（中文）

尽管大型语言模型在多个领域取得了成功，但在传统中医学（TCM）中的潜力仍未得到充分探索，主要面临两个关键障碍：一是高质量中医数据的稀缺，二是中医诊断的多模态特性，包括视觉、听觉、嗅觉和脉搏检测。为了解决这些挑战，本文提出了ShizhenGPT，这是首个针对中医的多模态大型语言模型。为克服数据稀缺问题，我们整理了迄今为止最大的中医数据集，包含超过100GB的文本和200GB的多模态数据，包括120万张图像、200小时音频和生理信号。ShizhenGPT经过预训练和指令调优，具备深厚的中医知识和多模态推理能力。实验结果表明，ShizhenGPT在中医视觉理解方面领先于现有多模态大型语言模型，并在多个评估任务中表现优异。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统中医领域中大型语言模型的应用不足，特别是由于高质量中医数据稀缺和多模态诊断需求导致的挑战。现有方法无法有效处理中医的多种感官信息，限制了其应用潜力。

**核心思路**：论文提出的ShizhenGPT通过整合大规模的中医数据集，结合文本、图像、音频等多模态信息，旨在提升模型对中医知识的理解和推理能力。这种设计使得模型能够处理复杂的多模态输入，适应中医的诊断需求。

**技术框架**：ShizhenGPT的整体架构包括数据收集、预训练和指令调优三个主要阶段。首先，构建了包含文本、图像、音频和生理信号的多模态数据集；其次，进行模型的预训练以学习中医知识；最后，通过指令调优提升模型在特定任务上的表现。

**关键创新**：ShizhenGPT的最大创新在于其针对中医领域的多模态学习能力，能够统一处理视觉、听觉和生理信号等多种输入形式。这一特性使其在中医视觉理解和诊断方面具有显著优势，与传统的单一模态模型相比，具备更全面的感知能力。

**关键设计**：在模型设计中，采用了适应多模态输入的网络结构，并针对不同模态设置了特定的损失函数，以优化模型在多模态任务上的表现。此外，数据集的构建和清洗过程也确保了数据的高质量和多样性。

## 📊 实验亮点

实验结果表明，ShizhenGPT在中医资格考试和视觉诊断基准测试中表现优异，超越了同规模的其他大型语言模型，并与更大规模的专有模型竞争，展示了其在中医视觉理解方面的领先地位。这些结果表明ShizhenGPT在多模态理解和推理能力上的显著提升。

## 🎯 应用场景

ShizhenGPT的潜在应用场景包括中医诊断辅助系统、医学教育和研究等领域。通过提供更全面的多模态理解能力，该模型能够帮助医生更准确地进行诊断，并为中医领域的研究提供新的工具和视角。未来，该研究有望推动中医与现代医学的结合，提升整体医疗水平。

## 📄 摘要（原文）

> Despite the success of large language models (LLMs) in various domains, their potential in Traditional Chinese Medicine (TCM) remains largely underexplored due to two critical barriers: (1) the scarcity of high-quality TCM data and (2) the inherently multimodal nature of TCM diagnostics, which involve looking, listening, smelling, and pulse-taking. These sensory-rich modalities are beyond the scope of conventional LLMs. To address these challenges, we present ShizhenGPT, the first multimodal LLM tailored for TCM. To overcome data scarcity, we curate the largest TCM dataset to date, comprising 100GB+ of text and 200GB+ of multimodal data, including 1.2M images, 200 hours of audio, and physiological signals. ShizhenGPT is pretrained and instruction-tuned to achieve deep TCM knowledge and multimodal reasoning. For evaluation, we collect recent national TCM qualification exams and build a visual benchmark for Medicinal Recognition and Visual Diagnosis. Experiments demonstrate that ShizhenGPT outperforms comparable-scale LLMs and competes with larger proprietary models. Moreover, it leads in TCM visual understanding among existing multimodal LLMs and demonstrates unified perception across modalities like sound, pulse, smell, and vision, paving the way toward holistic multimodal perception and diagnosis in TCM. Datasets, models, and code are publicly available. We hope this work will inspire further exploration in this field.

