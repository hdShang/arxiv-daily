---
layout: default
title: "Anatomy-R1: Enhancing Anatomy Reasoning in Multimodal Large Language Models via Anatomical Similarity Curriculum and Group Diversity Augmentation"
---

# Anatomy-R1: Enhancing Anatomy Reasoning in Multimodal Large Language Models via Anatomical Similarity Curriculum and Group Diversity Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19512" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19512v1</a>
  <a href="https://arxiv.org/pdf/2512.19512.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19512v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19512v1', 'Anatomy-R1: Enhancing Anatomy Reasoning in Multimodal Large Language Models via Anatomical Similarity Curriculum and Group Diversity Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyang Song, Zelin Zang, Zuyao Chen, Xusheng Liang, Dong Yi, Jinlin Wu, Hongbin Liu, Jiebo Luo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-22

**🔗 代码/项目**: [GITHUB](https://github.com/tomato996/Anatomy-R1)

---

## 💡 一句话要点

**Anatomy-R1：通过解剖相似性课程学习和群体多样性增强提升多模态大语言模型中的解剖推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `医学图像理解` `解剖推理` `课程学习` `数据增强` `视觉问答` `医学影像辅助诊断`

## 📋 核心要点

1. 医学图像解剖理解任务对模型提出了更高的精度和临床连贯性要求，但医学数据复杂且高质量标注稀缺，限制了现有监督微调方法的有效性。
2. 论文提出解剖相似性课程学习和群体多样性问题增强两种方法，前者通过渐进式学习提升模型掌握复杂问题的能力，后者扩展搜索空间，避免模型收敛到单一推理路径。
3. 在SGG-VQA和OmniMedVQA基准测试中，Anatomy-R1方法取得了显著的性能提升，验证了其在增强多模态大语言模型医学推理能力方面的有效性。

## 📝 摘要（中文）

多模态大语言模型(MLLMs)在自然图像推理方面取得了显著进展，但其在医学成像，特别是临床解剖手术图像中的潜力仍未被充分探索。解剖理解任务需要精确的理解和临床上连贯的答案，由于医学数据的复杂性和高质量专家注释的稀缺性，这些都难以实现。这些挑战限制了传统监督微调(SFT)策略的有效性。虽然最近的工作表明，群体相对策略优化(GRPO)可以在不依赖大量数据的情况下增强MLLM中的推理能力，但我们发现两个弱点阻碍了GRPO在解剖识别中的推理性能：1)知识不能在不同的解剖结构之间有效地共享，导致信息增益不均匀，并阻止模型收敛，以及2)模型迅速收敛到单一的推理路径，抑制了对多样化策略的探索。为了克服这些挑战，我们提出了两种新方法。首先，我们通过控制答案选择的相似性来控制问题的难度，从而实现一种称为解剖相似性课程学习的渐进式学习策略，使模型能够逐步掌握复杂的问题。其次，我们利用问题增强，即群体多样性问题增强，来扩展模型对困难查询的搜索空间，从而减轻产生统一响应的趋势。在SGG-VQA和OmniMedVQA基准上的综合实验表明，我们的方法在这两个基准上都取得了显著的改进，证明了其在增强MLLM的医学推理能力方面的有效性。代码可在https://github.com/tomato996/Anatomy-R1 找到。

## 🔬 方法详解

**问题定义**：现有方法在医学图像解剖理解任务中，由于医学数据的复杂性和标注的稀缺性，难以实现精确的理解和临床上连贯的答案。特别是，基于群体相对策略优化(GRPO)的方法，存在知识共享不足和推理路径单一的问题，导致模型难以收敛和探索多样化的解题策略。

**核心思路**：论文的核心思路是通过课程学习和数据增强，引导模型逐步学习和探索更广泛的解剖知识。解剖相似性课程学习模拟人类学习过程，从简单到复杂，逐步提升模型能力。群体多样性问题增强则鼓励模型探索不同的推理路径，避免陷入局部最优。

**技术框架**：Anatomy-R1方法主要包含两个阶段：解剖相似性课程学习和群体多样性问题增强。在解剖相似性课程学习阶段，根据答案选项的解剖相似性对问题进行排序，模型先学习相似性高的问题，再逐步学习相似性低的问题。在群体多样性问题增强阶段，针对困难问题，生成多个不同的问题变体，扩大模型的搜索空间。

**关键创新**：论文的关键创新在于将课程学习和数据增强相结合，并针对医学图像解剖理解任务的特点进行了定制化设计。解剖相似性课程学习利用解剖结构的相似性来控制学习难度，更符合医学知识的特点。群体多样性问题增强则通过生成多样化的提问方式，鼓励模型探索不同的推理路径。

**关键设计**：解剖相似性课程学习的关键在于如何衡量解剖结构的相似性，论文中具体如何实现未知。群体多样性问题增强的关键在于如何生成高质量的问题变体，论文中具体如何实现未知。损失函数和网络结构等细节未在摘要中提及，具体实现未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19512v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19512v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19512v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Anatomy-R1方法在SGG-VQA和OmniMedVQA两个医学视觉问答基准测试中取得了显著的性能提升，证明了其在增强多模态大语言模型医学推理能力方面的有效性。具体提升幅度未知，需要在论文中进一步查找。

## 🎯 应用场景

该研究成果可应用于医学影像辅助诊断、手术导航、医学教育等领域。通过提升多模态大语言模型对医学图像的理解能力，可以帮助医生更准确地识别病灶、制定治疗方案，并为医学教育提供更智能化的工具。未来，该技术有望在远程医疗、智能健康管理等方面发挥更大的作用。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved impressive progress in natural image reasoning, yet their potential in medical imaging remains underexplored, especially in clinical anatomical surgical images. Anatomy understanding tasks demand precise understanding and clinically coherent answers, which are difficult to achieve due to the complexity of medical data and the scarcity of high-quality expert annotations. These challenges limit the effectiveness of conventional Supervised Fine-Tuning (SFT) strategies. While recent work has demonstrated that Group Relative Policy Optimization (GRPO) can enhance reasoning in MLLMs without relying on large amounts of data, we find two weaknesses that hinder GRPO's reasoning performance in anatomy recognition: 1) knowledge cannot be effectively shared between different anatomical structures, resulting in uneven information gain and preventing the model from converging, and 2) the model quickly converges to a single reasoning path, suppressing the exploration of diverse strategies. To overcome these challenges, we propose two novel methods. First, we implement a progressive learning strategy called Anatomical Similarity Curriculum Learning by controlling question difficulty via the similarity of answer choices, enabling the model to master complex problems incrementally. Second, we utilize question augmentation referred to as Group Diversity Question Augmentation to expand the model's search space for difficult queries, mitigating the tendency to produce uniform responses. Comprehensive experiments on the SGG-VQA and OmniMedVQA benchmarks show our method achieves a significant improvement across the two benchmarks, demonstrating its effectiveness in enhancing the medical reasoning capabilities of MLLMs. The code can be found in https://github.com/tomato996/Anatomy-R1

