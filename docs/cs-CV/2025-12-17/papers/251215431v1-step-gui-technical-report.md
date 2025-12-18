---
layout: default
title: Step-GUI Technical Report
---

# Step-GUI Technical Report

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15431" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15431v1</a>
  <a href="https://arxiv.org/pdf/2512.15431.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15431v1" onclick="toggleFavorite(this, '2512.15431v1', 'Step-GUI Technical Report')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haolong Yan, Jia Wang, Xin Huang, Yeqing Shen, Ziyang Meng, Zhimin Fan, Kaijun Tan, Jin Gao, Lieyu Shi, Mi Yang, Shiliang Yang, Zhirui Wang, Brian Li, Kang An, Chenyang Li, Lei Lei, Mengmeng Duan, Danxun Liang, Guodong Liu, Hang Cheng, Hao Wu, Jie Dong, Junhao Huang, Mei Chen, Renjie Yu, Shunshan Li, Xu Zhou, Yiting Dai, Yineng Deng, Yingdan Liang, Zelin Chen, Wen Sun, Chengxu Yan, Chunqin Xu, Dong Li, Fengqiong Xiao, Guanghao Fan, Guopeng Li, Guozhen Peng, Hongbing Li, Hang Li, Hongming Chen, Jingjing Xie, Jianyong Li, Jingyang Zhang, Jiaju Ren, Jiayu Yuan, Jianpeng Yin, Kai Cao, Liang Zhao, Liguo Tan, Liying Shi, Mengqiang Ren, Min Xu, Manjiao Liu, Mao Luo, Mingxin Wan, Na Wang, Nan Wu, Ning Wang, Peiyao Ma, Qingzhou Zhang, Qiao Wang, Qinlin Zeng, Qiong Gao, Qiongyao Li, Shangwu Zhong, Shuli Gao, Shaofan Liu, Shisi Gao, Shuang Luo, Xingbin Liu, Xiaojia Liu, Xiaojie Hou, Xin Liu, Xuanti Feng, Xuedan Cai, Xuan Wen, Xianwei Zhu, Xin Liang, Xin Liu, Xin Zhou, Yingxiu Zhao, Yukang Shi, Yunfang Xu, Yuqing Zeng, Yixun Zhang, Zejia Weng, Zhonghao Yan, Zhiguo Huang, Zhuoyu Wang, Zheng Ge, Jing Li, Yibo Zhu, Binxing Jiao, Xiangyu Zhang, Daxin Jiang

**分类**: cs.CV

**发布日期**: 2025-12-17

**备注**: 41 pages, 26 figures

---

## 💡 一句话要点

**提出Step-GUI，通过自进化训练和GUI-MCP协议，实现高效、安全、通用的GUI自动化。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI自动化` `自进化学习` `多模态大语言模型` `隐私保护` `人机交互`

## 📋 核心要点

1. 现有GUI自动化方法缺乏高效、可靠的数据获取途径，标注成本高且质量难以保证。
2. 论文提出基于校准步奖励系统的自进化训练流水线，将模型生成的轨迹转化为可靠的训练信号，大幅降低标注成本。
3. Step-GUI模型在多个GUI基准测试中取得领先性能，并在AndroidDaily基准上验证了其在真实场景中的有效性。

## 📝 摘要（中文）

本文提出了一种基于校准步奖励系统的自进化训练流水线，以低成本获取高质量的GUI自动化训练数据，准确率超过90%。基于此，构建了Step-GUI模型家族（4B/8B），在AndroidWorld（80.2%）、OSWorld（48.5%）和ScreenShot-Pro（62.6%）等GUI基准测试中达到SOTA性能，并保持了强大的通用能力。为了在异构设备上实现标准化接口和保护用户隐私，提出了GUI-MCP协议，该协议采用分层架构，结合低级原子操作和高级任务委托给本地专家模型，实现高隐私的本地执行。此外，引入了AndroidDaily基准，评估智能体在真实日常使用场景中的性能（8B：静态89.91%，端到端52.50%）。该研究推动了实用GUI智能体的发展，并展示了在日常数字交互中实际部署的巨大潜力。

## 🔬 方法详解

**问题定义**：现有GUI自动化方法面临数据获取难题，标注成本高昂且标注质量难以保证，限制了模型性能的提升。同时，在实际部署中，需要考虑异构设备的兼容性和用户隐私保护问题。

**核心思路**：论文的核心思路是利用模型自身生成的数据，通过校准步奖励系统进行筛选和校正，构建高质量的训练数据集，从而实现模型的自进化。同时，设计GUI-MCP协议，将任务分解为低级原子操作和高级任务委托，在本地执行敏感操作，保护用户隐私。

**技术框架**：整体框架包含三个主要部分：1) 自进化训练流水线，利用校准步奖励系统生成和筛选训练数据；2) Step-GUI模型家族，基于Transformer架构，利用多模态输入进行GUI操作预测；3) GUI-MCP协议，实现跨平台兼容和隐私保护。

**关键创新**：最重要的技术创新点在于校准步奖励系统，它能够有效地将模型生成的轨迹转化为可靠的训练信号，大幅降低了数据标注成本。此外，GUI-MCP协议的设计也为GUI智能体的实际部署提供了新的思路。

**关键设计**：校准步奖励系统通过对模型生成轨迹的每一步进行评估，并根据评估结果调整奖励信号，从而筛选出高质量的轨迹。GUI-MCP协议采用分层架构，将任务分解为原子操作和高级任务，并利用本地专家模型处理敏感数据，保证用户隐私。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15431v1/figs/intro_head2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15431v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15431v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Step-GUI模型在AndroidWorld、OSWorld和ScreenShot-Pro等GUI基准测试中取得了显著的性能提升，其中8B模型在AndroidWorld上达到了80.2%的准确率。在更贴近真实场景的AndroidDaily基准测试中，8B模型在静态动作预测和端到端任务完成方面分别达到了89.91%和52.50%的准确率，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究成果可应用于智能手机、平板电脑等移动设备的自动化操作，例如自动完成任务、辅助用户操作等。此外，还可以应用于智能家居、智能车载等领域，实现设备的自动化控制和管理。该研究有望提升人机交互的效率和便捷性，并推动GUI智能体的广泛应用。

## 📄 摘要（原文）

> Recent advances in multimodal large language models unlock unprecedented opportunities for GUI automation. However, a fundamental challenge remains: how to efficiently acquire high-quality training data while maintaining annotation reliability? We introduce a self-evolving training pipeline powered by the Calibrated Step Reward System, which converts model-generated trajectories into reliable training signals through trajectory-level calibration, achieving >90% annotation accuracy with 10-100x lower cost. Leveraging this pipeline, we introduce Step-GUI, a family of models (4B/8B) that achieves state-of-the-art GUI performance (8B: 80.2% AndroidWorld, 48.5% OSWorld, 62.6% ScreenShot-Pro) while maintaining robust general capabilities. As GUI agent capabilities improve, practical deployment demands standardized interfaces across heterogeneous devices while protecting user privacy. To this end, we propose GUI-MCP, the first Model Context Protocol for GUI automation with hierarchical architecture that combines low-level atomic operations and high-level task delegation to local specialist models, enabling high-privacy execution where sensitive data stays on-device. Finally, to assess whether agents can handle authentic everyday usage, we introduce AndroidDaily, a benchmark grounded in real-world mobile usage patterns with 3146 static actions and 235 end-to-end tasks across high-frequency daily scenarios (8B: static 89.91%, end-to-end 52.50%). Our work advances the development of practical GUI agents and demonstrates strong potential for real-world deployment in everyday digital interactions.

