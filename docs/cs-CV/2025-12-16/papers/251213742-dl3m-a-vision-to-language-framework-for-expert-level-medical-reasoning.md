---
layout: default
title: DL$^3$M: A Vision-to-Language Framework for Expert-Level Medical Reasoning through Deep Learning and Large Language Models
---

# DL$^3$M: A Vision-to-Language Framework for Expert-Level Medical Reasoning through Deep Learning and Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13742" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13742</a>
  <a href="https://arxiv.org/pdf/2512.13742.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13742" onclick="toggleFavorite(this, '2512.13742', 'DL$^3$M: A Vision-to-Language Framework for Expert-Level Medical Reasoning through Deep Learning and Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md. Najib Hasan, Imran Ahmad, Sourav Basak Shuvo, Md. Mahadi Hasan Ankon, Sunanda Das, Nazmul Siddique, Hui Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**DL$^3$M：结合深度学习与大语言模型，实现专家级医学推理的视觉-语言框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分类` `大型语言模型` `临床推理` `深度学习` `可解释性` `内窥镜图像` `MobileCoAtNet`

## 📋 核心要点

1. 医学图像分类器缺乏决策解释能力，而大型语言模型在视觉推理方面存在困难，导致模型推理与临床期望存在差距。
2. 提出DL$^3$M框架，通过结合图像分类与结构化临床推理，弥合模型所见与临床医生期望之间的差距。
3. 设计了MobileCoAtNet模型用于内窥镜图像分类，并在八个胃相关类别上取得了高精度，并构建了专家验证的推理基准。

## 📝 摘要（中文）

医学图像分类器在检测胃肠道疾病方面表现良好，但无法解释其决策过程。大型语言模型可以生成临床文本，但难以进行视觉推理，并且常常产生不稳定或不正确的解释。这导致模型所见与临床医生期望的推理类型之间存在差距。我们引入了一个框架，将图像分类与结构化的临床推理联系起来。我们设计了一种新的混合模型MobileCoAtNet，专门用于内窥镜图像，并在八个与胃相关的类别中实现了高精度。其输出被用于驱动多个大型语言模型的推理。为了评估这种推理，我们构建了两个经过专家验证的基准，涵盖病因、症状、治疗、生活方式和随访护理。我们针对这些黄金标准评估了32个大型语言模型。强大的分类能力提高了它们解释的质量，但没有一个模型达到人类水平的稳定性。即使是最好的大型语言模型，在提示发生变化时也会改变其推理。我们的研究表明，将深度学习与大型语言模型相结合可以产生有用的临床叙述，但目前的大型语言模型对于高风险的医疗决策仍然不可靠。该框架提供了一个更清晰的视角来了解它们的局限性，并为构建更安全的推理系统提供了一条途径。本研究中使用的完整源代码和数据集可在指定网址获取。

## 🔬 方法详解

**问题定义**：现有医学图像分类器虽然能有效检测疾病，但缺乏可解释性，无法提供决策依据。大型语言模型虽然能生成临床文本，但在视觉推理方面表现不足，容易产生不准确或不稳定的解释。这导致模型输出与临床医生的期望存在鸿沟，阻碍了其在实际医疗场景中的应用。

**核心思路**：DL$^3$M框架的核心在于将图像分类与结构化的临床推理相结合。首先，利用深度学习模型对医学图像进行精确分类，提取关键视觉特征。然后，将这些特征作为输入，驱动大型语言模型进行推理，生成包含病因、症状、治疗等信息的临床叙述。通过这种方式，弥合了视觉信息与临床推理之间的差距，提高了模型的可解释性和实用性。

**技术框架**：DL$^3$M框架主要包含两个阶段：图像分类阶段和语言推理阶段。在图像分类阶段，使用MobileCoAtNet模型对内窥镜图像进行分类，输出图像所属的类别以及相应的置信度。在语言推理阶段，将图像分类的结果作为提示（prompt）输入到大型语言模型中，引导其生成结构化的临床叙述。框架还包括两个专家验证的基准数据集，用于评估大型语言模型推理的质量和稳定性。

**关键创新**：该论文的关键创新在于提出了一个将深度学习图像分类与大型语言模型推理相结合的框架，并针对医学领域的特殊需求进行了优化。MobileCoAtNet模型的设计以及专家验证的推理基准的构建，都为该框架的有效性提供了保障。此外，该研究还深入分析了现有大型语言模型在医学推理方面的局限性，为未来研究方向提供了指导。

**关键设计**：MobileCoAtNet模型是基于CoAtNet架构改进而来，针对内窥镜图像的特点进行了优化。具体的技术细节包括：采用了MobileNetV2的倒残差模块以减少计算量，使用了更大的卷积核以捕获更丰富的上下文信息，并引入了注意力机制以增强模型的特征表达能力。在语言推理阶段，使用了不同的提示策略来引导大型语言模型生成临床叙述，并对不同模型的推理结果进行了详细的对比分析。损失函数未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13742/Figures/DL_vs_LLM_comparison.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13742/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13742/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MobileCoAtNet模型在内窥镜图像分类任务中取得了优异的性能，并在八个胃相关类别上实现了高精度。对32个大型语言模型的评估结果显示，强大的分类能力可以提高其解释的质量，但没有一个模型达到人类水平的稳定性。即使是最好的大型语言模型，在提示发生变化时也会改变其推理，表明当前的大型语言模型在医学推理方面仍存在局限性。

## 🎯 应用场景

该研究成果可应用于辅助医生进行疾病诊断和治疗方案制定，提高诊断效率和准确性。通过提供可解释的临床推理，增强医生对AI系统的信任度。此外，该框架还可用于构建智能化的医学教育和培训系统，帮助医学生更好地理解疾病的病理机制和临床表现。未来，该研究有望推动AI技术在医疗领域的更广泛应用。

## 📄 摘要（原文）

> Medical image classifiers detect gastrointestinal diseases well, but they do not explain their decisions. Large language models can generate clinical text, yet they struggle with visual reasoning and often produce unstable or incorrect explanations. This leaves a gap between what a model sees and the type of reasoning a clinician expects. We introduce a framework that links image classification with structured clinical reasoning. A new hybrid model, MobileCoAtNet, is designed for endoscopic images and achieves high accuracy across eight stomach-related classes. Its outputs are then used to drive reasoning by several LLMs. To judge this reasoning, we build two expert-verified benchmarks covering causes, symptoms, treatment, lifestyle, and follow-up care. Thirty-two LLMs are evaluated against these gold standards. Strong classification improves the quality of their explanations, but none of the models reach human-level stability. Even the best LLMs change their reasoning when prompts vary. Our study shows that combining DL with LLMs can produce useful clinical narratives, but current LLMs remain unreliable for high-stakes medical decisions. The framework provides a clearer view of their limits and a path for building safer reasoning systems. The complete source code and datasets used in this study are available atthis https URL.

