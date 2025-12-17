---
layout: default
title: Code2Video: A Code-centric Paradigm for Educational Video Generation
---

# Code2Video: A Code-centric Paradigm for Educational Video Generation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01174" target="_blank" class="toolbar-btn">arXiv: 2510.01174v1</a>
    <a href="https://arxiv.org/pdf/2510.01174.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01174v1" 
            onclick="toggleFavorite(this, '2510.01174v1', 'Code2Video: A Code-centric Paradigm for Educational Video Generation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yanzhe Chen, Kevin Qinghong Lin, Mike Zheng Shou

**分类**: cs.CV, cs.AI, cs.CL, cs.HC, cs.MM

**发布日期**: 2025-10-01

**备注**: Project Page: https://showlab.github.io/Code2Video/

**🔗 代码/项目**: [GITHUB](https://github.com/showlab/Code2Video)

---

## 💡 一句话要点

**提出Code2Video框架，通过可执行代码生成专业教育视频，提升可控性和教学质量。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `教育视频生成` `代码生成` `视觉语言模型` `程序化生成` `可控视频生成`

## 📋 核心要点

1. 现有视频生成模型难以满足教育视频对学科知识、视觉结构和连贯性的要求。
2. Code2Video通过可执行Python代码控制渲染环境，生成具有精确视觉结构和连贯过渡的教育视频。
3. 实验表明，Code2Video在代码效率和教学质量上均优于直接代码生成，并接近人工制作水平。

## 📝 摘要（中文）

现有的生成模型在像素空间视频合成方面取得了进展，但它们在生成专业教育视频方面仍然存在局限性，因为教育视频需要学科知识、精确的视觉结构和连贯的过渡，这限制了它们在教育场景中的应用。本文提出Code2Video，这是一个以代码为中心的代理框架，通过可执行的Python代码生成教育视频。该框架包含三个协作代理：（i）规划器，将讲座内容构建成时间上连贯的流程并准备相应的视觉资产；（ii）编码器，将结构化指令转换为可执行的Python代码，同时结合范围引导的自动修复以提高效率；（iii）评论器，利用带有视觉锚点提示的视觉语言模型（VLM）来细化空间布局并确保清晰度。为了支持系统评估，我们构建了MMMC，这是一个专业制作的、特定学科的教育视频基准。我们在MMMC上评估了多个维度，包括VLM作为评判者的美学分数、代码效率，以及特别是TeachQuiz，这是一种新颖的端到端指标，用于量化VLM在取消学习后，通过观看生成的视频可以恢复多少知识。结果表明，Code2Video具有作为一种可扩展、可解释和可控方法的潜力，与直接代码生成相比提高了40%，并且生成的视频可与人工制作的教程相媲美。代码和数据集可在https://github.com/showlab/Code2Video获取。

## 🔬 方法详解

**问题定义**：现有视频生成模型难以生成高质量的教育视频，因为教育视频需要精确的视觉结构、学科知识和连贯的过渡。直接从文本或像素生成视频难以保证这些特性，并且缺乏可控性和可解释性。

**核心思路**：Code2Video的核心思想是将教育视频的生成过程转化为一个可执行代码的生成和渲染过程。通过编写Python代码来控制视频中的视觉元素和动画，从而实现对视频内容和风格的精确控制。这种方法借鉴了程序化生成和基于规则的动画制作的思想，将视频生成过程变得更加可控、可解释和可扩展。

**技术框架**：Code2Video框架包含三个主要模块：规划器（Planner）、编码器（Coder）和评论器（Critic）。规划器负责将讲座内容分解为时间上连贯的流程，并准备相应的视觉资产。编码器将结构化指令转换为可执行的Python代码，并利用范围引导的自动修复来提高代码效率。评论器利用视觉语言模型（VLM）和视觉锚点提示来细化空间布局，确保视频的清晰度。整个流程是一个迭代的过程，编码器生成代码后，评论器会评估视频质量并提供反馈，编码器根据反馈进行调整，直到达到满意的效果。

**关键创新**：Code2Video的关键创新在于其以代码为中心的生成范式。与传统的直接从文本或像素生成视频的方法不同，Code2Video通过可执行代码来控制视频的生成过程，从而实现了对视频内容和风格的精确控制。此外，该框架还引入了范围引导的自动修复和视觉锚点提示等技术，进一步提高了代码效率和视频质量。

**关键设计**：规划器使用大型语言模型（LLM）将教学内容分解为一系列步骤，并确定每个步骤所需的视觉元素。编码器使用预训练的代码生成模型，并结合范围引导的自动修复来生成可执行的Python代码。评论器使用视觉语言模型（VLM）来评估视频质量，并提供关于空间布局和清晰度的反馈。TeachQuiz指标用于评估生成的视频的教学效果，通过测试VLM在观看视频后恢复知识的能力来衡量视频的质量。

## 📊 实验亮点

Code2Video在MMMC基准测试中表现出色，与直接代码生成相比，性能提升了40%。通过TeachQuiz指标评估，生成的视频在教学质量上可与人工制作的教程相媲美。VLM-as-a-Judge美学分数也表明，Code2Video生成的视频具有较高的视觉质量。

## 🎯 应用场景

Code2Video可应用于大规模生成高质量的在线教育视频，降低教育资源制作成本，并实现个性化定制。该技术还可用于制作产品演示、软件教程等视频内容，具有广泛的应用前景。未来，该技术有望与虚拟现实、增强现实等技术结合，创造更加沉浸式的学习体验。

## 📄 摘要（原文）

> While recent generative models advance pixel-space video synthesis, they remain limited in producing professional educational videos, which demand disciplinary knowledge, precise visual structures, and coherent transitions, limiting their applicability in educational scenarios. Intuitively, such requirements are better addressed through the manipulation of a renderable environment, which can be explicitly controlled via logical commands (e.g., code). In this work, we propose Code2Video, a code-centric agent framework for generating educational videos via executable Python code. The framework comprises three collaborative agents: (i) Planner, which structures lecture content into temporally coherent flows and prepares corresponding visual assets; (ii) Coder, which converts structured instructions into executable Python codes while incorporating scope-guided auto-fix to enhance efficiency; and (iii) Critic, which leverages vision-language models (VLM) with visual anchor prompts to refine spatial layout and ensure clarity. To support systematic evaluation, we build MMMC, a benchmark of professionally produced, discipline-specific educational videos. We evaluate MMMC across diverse dimensions, including VLM-as-a-Judge aesthetic scores, code efficiency, and particularly, TeachQuiz, a novel end-to-end metric that quantifies how well a VLM, after unlearning, can recover knowledge by watching the generated videos. Our results demonstrate the potential of Code2Video as a scalable, interpretable, and controllable approach, achieving 40% improvement over direct code generation and producing videos comparable to human-crafted tutorials. The code and datasets are available at https://github.com/showlab/Code2Video.

