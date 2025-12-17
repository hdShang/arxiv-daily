---
layout: default
title: Solar PV Installation Potential Assessment on Building Facades Based on Vision and Language Foundation Models
---

# Solar PV Installation Potential Assessment on Building Facades Based on Vision and Language Foundation Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.00797" target="_blank" class="toolbar-btn">arXiv: 2510.00797v1</a>
    <a href="https://arxiv.org/pdf/2510.00797.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00797v1" 
            onclick="toggleFavorite(this, '2510.00797v1', 'Solar PV Installation Potential Assessment on Building Facades Based on Vision and Language Foundation Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ruyu Liu, Dongxu Zhuang, Jianhua Zhang, Arega Getaneh Abate, Per Sieverts Nielsen, Ben Wang, Xiufeng Liu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**提出SF-SPA框架，利用视觉-语言模型评估建筑立面的光伏安装潜力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `光伏潜力评估` `建筑立面` `计算机视觉` `大型语言模型` `语义分割`

## 📋 核心要点

1. 现有方法难以有效评估城市环境中建筑立面的光伏潜力，因为立面几何形状复杂且包含多种语义元素。
2. SF-SPA框架利用计算机视觉和大型语言模型，从街景图像中自动提取信息，进行光伏潜力评估。
3. 实验结果表明，SF-SPA框架在面积估计方面具有较高的准确性，且评估效率远高于人工方法。

## 📝 摘要（中文）

本研究提出了一个名为SF-SPA（语义立面太阳能光伏评估）的自动化框架，旨在将街景照片转化为光伏部署的定量评估。该框架结合了计算机视觉和人工智能技术，解决了三个关键挑战：透视失真校正、立面元素的语义理解以及光伏布局优化的空间推理。该方法包含四个阶段的流程：几何校正、零样本语义分割、大型语言模型（LLM）引导的空间推理和能量模拟。在四个国家/地区的80座建筑物上进行的验证表明，该方法具有强大的性能，与专家标注相比，平均面积估计误差为6.2% ± 2.8%。自动评估每栋建筑物大约需要100秒，与手动方法相比，效率大大提高。模拟的能量产量预测证实了该方法在区域潜力研究、城市能源规划和建筑集成光伏（BIPV）部署中的可靠性和适用性。

## 🔬 方法详解

**问题定义**：现有方法在评估城市建筑立面的光伏潜力时，面临着几何形状复杂、语义信息多样以及人工评估效率低下的问题。传统方法难以准确处理透视失真，无法有效理解立面元素的语义信息，导致评估结果不准确且耗时。

**核心思路**：SF-SPA框架的核心思路是利用计算机视觉技术进行图像预处理和特征提取，然后借助大型语言模型进行空间推理和布局优化。通过几何校正消除透视失真，利用零样本语义分割理解立面元素，最后使用LLM进行光伏板的空间布局优化，从而实现自动化的光伏潜力评估。

**技术框架**：SF-SPA框架包含四个主要阶段：1) 几何校正：使用图像处理技术校正街景图像的透视失真。2) 零样本语义分割：利用预训练的视觉模型对立面图像进行语义分割，识别出窗户、墙壁等元素。3) 大型语言模型引导的空间推理：使用LLM根据语义分割结果和建筑规则进行光伏板的空间布局优化。4) 能量模拟：根据光伏板的布局和当地的气候条件，模拟计算光伏系统的能量产量。

**关键创新**：该方法最重要的创新点在于将大型语言模型引入到光伏潜力评估中。LLM能够理解建筑规则和空间关系，从而实现更智能的光伏板布局优化。此外，该方法还采用了零样本语义分割技术，无需大量标注数据即可实现对立面元素的准确识别。

**关键设计**：在几何校正阶段，采用了基于消失点的透视变换方法。在零样本语义分割阶段，使用了CLIP模型进行图像特征提取和语义分类。在LLM引导的空间推理阶段，使用了Prompt Engineering技术，设计合适的Prompt来指导LLM进行布局优化。能量模拟阶段，使用了PVsyst软件进行光伏系统的性能评估。

## 📊 实验亮点

SF-SPA框架在80栋建筑上的验证结果显示，其面积估计误差仅为6.2% ± 2.8%，与专家标注结果高度吻合。与手动评估方法相比，SF-SPA框架的评估效率提高了数倍，每栋建筑的评估时间约为100秒。能量模拟结果表明，该方法能够准确预测光伏系统的能量产量，为实际应用提供了可靠的依据。

## 🎯 应用场景

该研究成果可应用于城市能源规划、建筑集成光伏（BIPV）部署、区域光伏潜力评估等领域。通过自动化评估建筑立面的光伏潜力，可以为城市规划者和建筑设计师提供决策支持，促进可再生能源的利用，助力实现可持续发展目标。此外，该方法还可以应用于光伏板制造商的产品推广和市场分析。

## 📄 摘要（原文）

> Building facades represent a significant untapped resource for solar energy generation in dense urban environments, yet assessing their photovoltaic (PV) potential remains challenging due to complex geometries and semantic com ponents. This study introduces SF-SPA (Semantic Facade Solar-PV Assessment), an automated framework that transforms street-view photographs into quantitative PV deployment assessments. The approach combines com puter vision and artificial intelligence techniques to address three key challenges: perspective distortion correction, semantic understanding of facade elements, and spatial reasoning for PV layout optimization. Our four-stage pipeline processes images through geometric rectification, zero-shot semantic segmentation, Large Language Model (LLM) guided spatial reasoning, and energy simulation. Validation across 80 buildings in four countries demonstrates ro bust performance with mean area estimation errors of 6.2% &#177; 2.8% compared to expert annotations. The auto mated assessment requires approximately 100 seconds per building, a substantial gain in efficiency over manual methods. Simulated energy yield predictions confirm the method's reliability and applicability for regional poten tial studies, urban energy planning, and building-integrated photovoltaic (BIPV) deployment. Code is available at: https:github.com/CodeAXu/Solar-PV-Installation

